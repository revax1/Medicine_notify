from __future__ import division

from Utils import *
from UI_Generate import *

from PyQt5.QtCore import QThread, pyqtSignal, QObject

import sys
import time
import RPi.GPIO as GPIO

from datetime import datetime
import os
import Adafruit_PCA9685
import subprocess
import threading
import requests
import pygame

import sqlite3
import json

########################### Thread ###########################
class SensorThread(QObject):
    finished = pyqtSignal()
    current_time_signal = pyqtSignal(bool)
    
    def __init__(self, parent=None):
        
        super(SensorThread, self).__init__(parent)
        # self.run_thread()
        
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        #set GPIO Pins Ultrasonic Sensor
        self.GPIO_TRIGGER = 18 
        self.GPIO_ECHO = 24

        #set GPIO Pins Motion Sensor
        self.GPIO_PIR = 6

        # #et GPIO Pins LED
        self.led_pin = 16
        
        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        GPIO.setup(self.GPIO_PIR, GPIO.IN)
        GPIO.setup(self.led_pin, GPIO.OUT)
        
        self.is_running = True
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.servo_min = 150
        self.servo_max = 600
        self.servo_drop = 350
        self.max_col = 7
        self.max_row = 5
        self.distance_value = 999999999             # สร้างค่าคงที่ของระยะอัลตร้าโซนิคเริ่มต้น
        self.all_drug_empty = False
        self.is_new_day = False
        self.previous_day = datetime.now().date()
        
        self.beep_event = threading.Event()             # สร้าง Event สำหรับการมารับยา
        self.distance_event = threading.Event()
        self.motion_detect_event = threading.Event()     
        
        self.state_file = '/home/pi/Documents/Medicine_notify/state/servo_state.txt'
        self.prepare_state_file = '/home/pi/Documents/Medicine_notify/state/prepare_state.txt'
        self.main_state_file = '/home/pi/Documents/Medicine_notify/state/main_state.txt'
        self.notify_state_file = '/home/pi/Documents/Medicine_notify/state/notify_state.txt'
        self.meal_drug_list_file = '/home/pi/Documents/Medicine_notify/state/meal_drug_list.json'
        
        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)
        
    ####################### สำหรับ Ultrasonic Sensor ########################

    def distance(self):
        while self.is_running:
            if self.distance_event.is_set():
                # set Trigger to HIGH
                GPIO.output(self.GPIO_TRIGGER, True)
            
                # set Trigger after 0.01ms to LOW
                time.sleep(0.00001)
                GPIO.output(self.GPIO_TRIGGER, False)
            
                StartTime = time.time()
                StopTime = time.time()
            
                # save StartTime
                while GPIO.input(self.GPIO_ECHO) == 0:
                    StartTime = time.time()
            
                # save time of arrival
                while GPIO.input(self.GPIO_ECHO) == 1:
                    StopTime = time.time()
            
                # time difference between start and arrival
                TimeElapsed = StopTime - StartTime
                # multiply with the sonic speed (34300 cm/s)
                # and divide by 2, because there and back
                self.distance_value = (TimeElapsed * 34300) / 2
                
                # print("Measured Distance = %.1f cm" % self.distance_value)
                time.sleep(1)

    ########################## สำหรับ PIR Sensor ############################

    def motion_detect(self):
        while self.is_running:
            if self.motion_detect_event.is_set():
                if GPIO.input(self.GPIO_PIR):              # Check whether pir is HIGH
                    # print("Motion Detected!")
                    pass
                else:
                    # print("No Motion Detected!")
                    pass
            else:
                time.sleep(1)

    ########################## สำหรับ Servo Motor ###########################
    # Initialise the PCA9685 using the default address (0x40).

    # Alternatively specify a different address and/or bus:
    #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

    # Configure min and max servo pulse lengths

    def save_state(self, col, row, servoNum):
        with open(self.state_file, 'w') as f:
            f.write(f'{col},{row},{servoNum}')

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                content = f.read().split(',')
                state = (int(content[0]), int(content[1]), int(content[2]))
                # print(f'Loaded state: {state[0]},{state[1]},{state[2]}')
                return state
        return 0, 0, 0  # default values if the file doesn't exist
    
    def load_prepare_state(self):
        if os.path.exists(self.prepare_state_file):
            with open(self.prepare_state_file, 'r') as f:
                content = f.read().strip()
                state = content == 'True'
                # print(f'Loaded state: {state}')
                return state
        return False
    
    def save_prepare_state(self, prepare):
        prepare_str = 'True' if prepare else 'False'
        with open(self.prepare_state_file, 'w') as f:
            f.write(prepare_str)
    
    def save_main_state(self, prepare):
        prepare_str = 'True' if prepare else 'False'
        with open(self.main_state_file, 'w') as f:
            f.write(prepare_str)
            
    def save_notify_state(self, prepare):
        prepare_str = 'True' if prepare else 'False'
        with open(self.notify_state_file, 'w') as f:
            f.write(prepare_str)
            
    def load_meal_drug_list(self):
        if os.path.exists(self.meal_drug_list_file):
                with open(self.meal_drug_list_file, 'r', encoding='utf-8') as f:
                    content = json.load(f)
                    return content
        return []
    
    def save_meal_drug_list(self, prepare_list):
        prepare_str = json.dumps(prepare_list, ensure_ascii=False)
        with open(self.meal_drug_list_file, 'w', encoding='utf-8') as f:
            f.write(prepare_str)

    ############################# สำหรับ Audio ##############################

    def get_drug(self):
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/get_drug.mp3")
        # pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/get_drug.m4a")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    def beep_audio(self):
        while self.is_running:
            if self.beep_event.is_set():
                    # Initialize Pygame
                    pygame.init()
                    clock = pygame.time.Clock()

                    # Set the duration to 1 minute (60,000 milliseconds)

                    pygame.mixer.init()
                    pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/beep.mp3")
                    pygame.mixer.music.play()
                    # time.sleep(3)

                    # Wait for the sound to finish playing
                    while pygame.mixer.music.get_busy():
                        clock.tick(1)

                    # Clean up Pygame
                    pygame.mixer.quit()
                    pygame.quit()
            else:
                time.sleep(1)
            time.sleep(1)
        

    def fg_bb(self):
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bb.mp3")
        # pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bb.m4a")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
    
    def fg_ab(self):
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_ab.mp3")
        # pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_ab.m4a")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    def fg_bl(self):
                # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bl.mp3")
        # pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bl.m4a")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    def fg_al(self):
                # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_al.mp3")
        # pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_al.m4a")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    def fg_bd(self):
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bd.mp3")
        # pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bd.m4a")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    def fg_ad(self):
                # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_ad.mp3")
        # pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_ad.m4a")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    def fg_bbed(self):
                # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bbed.mp3")
        # pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bbed.m4a")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    ########################### สำหรับรัน Server #############################

    def server(self):
        subprocess.run(["/home/pi/Documents/Medicine_notify/src/server.sh"])
        
    ############################# สำหรับถ่ายภาพ ##############################
    
    def capture_image(self):
        subprocess.run(["/home/pi/Documents/Medicine_notify/src/capture_image.sh"])


    ############################ LED #######################################

    def led_blink(self):
        # Toggle the LED based on the current time
        GPIO.output(self.led_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.led_pin, GPIO.LOW)
        time.sleep(0.5)
        
    ##################### สำหรับ Line Messaging API #########################

    def get_drug_line(self, channel_access_token, meal_name):
        url = "https://api.line.me/v2/bot/message/broadcast"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + channel_access_token,
        }

        data = {
            "messages": [
                {
                    "type": "text",
                    "text": f"ถึงเวลารับประทานยา {meal_name}"
                }
            ],
        }
        
        response = requests.post(url, headers=headers, json=data)
    
    # ส่งรูปภาพเมื่อมารับยา
    def send_image_to_line(self, image_url, channel_access_token, meal_name):
        url = "https://api.line.me/v2/bot/message/broadcast"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + channel_access_token,
        }

        data = {
            "messages": [
                {
                    "type": "text",
                    "text": f"ผู้สูงอายุมารับ ยา{meal_name}แล้ว"
                },
                {   
                    "type": "image",
                    "originalContentUrl": image_url,
                    "previewImageUrl": image_url,
                } 
            ],
        }
        
        response = requests.post(url, headers=headers, json=data)
        
    def not_receive_line(self, channel_access_token, meal_name):
        url = "https://api.line.me/v2/bot/message/broadcast"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + channel_access_token,
        }

        data = {
            "messages": [
                {
                    "type": "text",
                    "text": f"ผู้สูงอายุไม่ได้มารับยา{meal_name}"
                }
            ],
        }
        
        response = requests.post(url, headers=headers, json=data)
        
    def wait_receive_line(self, channel_access_token, number):
        url = "https://api.line.me/v2/bot/message/broadcast"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + channel_access_token,
        }
        data = {
            "messages": [
                {
                    "type": "text",
                    "text": f"แจ้งเตือนครั้งที่ {number} ผู้สูงอายุยังไม่มารับยาใน {number*5} นาทีนี้",
                }
            ],
        }
        
        response = requests.post(url, headers=headers, json=data)
        
    ########################################################################

    def load_meal_times_from_database(self):
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
        cursor = connection.cursor()

        # cursor.execute("SELECT meal_name, time FROM Meal")
        cursor.execute('''SELECT m.meal_name, m.time FROM Meal AS m
                        JOIN Drug_handle AS h ON m.meal_id = h.meal_id
                        WHERE h.meal_id''')
        
        drugs = cursor.fetchall()

        meal_times = {}
        for meal_name, time_str in drugs:
            # แปลงเวลาจากฐานข้อมูลให้อยู่ในรูปแบบที่ต้องการ
            time_obj = datetime.strptime(time_str, "%H:%M")
            time_formatted = time_obj.strftime("%H:%M:%S")
            meal_times[meal_name] = time_formatted

        # print(meal_times)
        connection.close()

        return meal_times
    
    ########################################################################
    
    def run(self):
        
        def time_to_seconds(time_str):
            # แปลงข้อความวันที่เป็นวัตถุเวลา
            time_obj = datetime.strptime(time_str, "%H:%M:%S")
            # หาจำนวนวินาทีที่ผ่านไปตั้งแต่เที่ยงคืน
            seconds = (time_obj - datetime(time_obj.year, time_obj.month, time_obj.day)).total_seconds()
            return seconds
        
        
        def update_meal_seconds():
            while True:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                self.meal_seconds = time_to_seconds(current_time)

        update_thread = threading.Thread(target=update_meal_seconds)
        update_thread.start()

        GPIO.output(self.led_pin, GPIO.LOW)
        
        bb_not_receive = False
        ab_not_receive = False
        bl_not_receive = False
        al_not_receive = False
        bd_not_receive = False
        ad_not_receive = False
        bbed_not_receive = False
        
        before_breakfast_seconds = 99999.0
        after_breakfast_seconds = 99999.0
        before_lunch_seconds = 99999.0
        after_lunch_seconds = 99999.0
        before_dinner_seconds = 99999.0
        after_dinner_seconds = 99999.0
        before_sleep_seconds = 99999.0
        
        before_breakfast_time = False
        after_breakfast_time = False
        before_lunch_time = False
        after_lunch_time = False
        before_dinner_time = False
        after_dinner_time = False
        before_sleep_time = False
        
        meal_times = self.load_meal_times_from_database()
        
        # Access meal times using the meal names
        before_breakfast = meal_times.get("มื้อเช้า ก่อนอาหาร", "")
        after_breakfast = meal_times.get("มื้อเช้า หลังอาหาร", "")
        before_lunch = meal_times.get("มื้อเที่ยง ก่อนอาหาร", "")
        after_lunch = meal_times.get("มื้อเที่ยง หลังอาหาร", "")
        before_dinner = meal_times.get("มื้อเย็น ก่อนอาหาร", "")
        after_dinner = meal_times.get("มื้อเย็น หลังอาหาร", "")
        before_sleep = meal_times.get("มื้อก่อนนอน", "")
        
        time_flags = {
            "before_breakfast_time": False,
            "after_breakfast_time": False,
            "before_lunch_time": False,
            "after_lunch_time": False,
            "before_dinner_time": False,
            "after_dinner_time": False,
            "before_sleep_time": False
        }
        
        if not before_breakfast == "":
            before_breakfast_seconds = time_to_seconds(before_breakfast)
            before_breakfast_time = True
            time_flags["before_breakfast_time"] = True
        if not after_breakfast == "":    
            after_breakfast_seconds = time_to_seconds(after_breakfast)
            after_breakfast_time = True
            time_flags["after_breakfast_time"] = True
        if not before_lunch == "":
            before_lunch_seconds = time_to_seconds(before_lunch)
            before_lunch_time = True
            time_flags["before_lunch_time"] = True
        if not after_lunch == "":
            after_lunch_seconds = time_to_seconds(after_lunch)
            after_lunch_time = True
            time_flags["after_lunch_time"] = True
        if not before_dinner == "":
            before_dinner_seconds = time_to_seconds(before_dinner)
            before_dinner_time = True
            time_flags["before_dinner_time"] = True
        if not after_dinner == "":
            after_dinner_seconds = time_to_seconds(after_dinner)
            after_dinner_time = True
            time_flags["after_dinner_time"] = True
        if not before_sleep == "":
            before_sleep_seconds = time_to_seconds(before_sleep)
            before_sleep_time = True
            time_flags["before_sleep_time"] = True
        
        # รัน Process แบบ Multithread   
        web_server_thread = threading.Thread(target=self.server)
        # รัน web_server
        web_server_thread.start()

        # Channel Access Token และ URL ของไฟล์สำหรับเก็บรูปภาพใน Line
        self.ngrok_url = "https://secure-zebra-lately.ngrok-free.app/"
        self.image_url = "https://secure-zebra-lately.ngrok-free.app/image.jpg"
        self.channel_access_token = "7llX7K06pe0vyog2sWuF/5ool/qx2unEmFCz6ZVYSRYtH5rhkzAIIl5MWZEzXBeV9Xc2cKRzPqMbHGvrfjQDuO4ku98MgbPD8arM9MaJWm8M7RuoPJgavG/aQuJ+Tu5CsYNbSf/GkLPrtGLkFBV6YgdB04t89/1O/w1cDnyilFU="

        # self.send_request_with_header(self.ngrok_url, 'ngrok-skip-browser-warning', 'true')       # ให้ skip หน้าเว็บ warning
        self.distance_thread = threading.Thread(target=self.distance)
        self.motion_thread = threading.Thread(target=self.motion_detect)
        self.audio_thread = threading.Thread(target=self.beep_audio)
        
        self.distance_thread.start()
        self.motion_thread.start()
        self.audio_thread.start()
        
        try:
            while True:
                
                # cur_col, cur_row, servoNum = self.load_state()
                # self.pwm.set_pwm(servoNum, 0, self.servo_max)      
                # self.pwm.set_pwm(servoNum + 1, 0, self.servo_max)
                
                self.all_drug_empty = False
                self.get_prepare = self.load_prepare_state()
                while self.get_prepare:
                    
                    if self.all_drug_empty:
                        break
                    
                    meal_times = self.load_meal_times_from_database()
                    meal_drug_list = self.load_meal_drug_list()
                    
                    selected_items = []
                    cur_col, cur_row, servoNum = self.load_state()

                    for check_col, check_row, drug_id, drug_name, meal_id, meal_name, meal_time, state in meal_drug_list:
                        if check_col == cur_col and check_row == cur_row:
                            selected_items.append((check_col, check_row, drug_id, drug_name, meal_id, meal_name, meal_time))
                    
                    cur_meal_name = selected_items[-1][5]
                    cur_meal_time = meal_times.get(f"{cur_meal_name}", "")

                    before_breakfast = meal_times.get("มื้อเช้า ก่อนอาหาร", "")
                    after_breakfast = meal_times.get("มื้อเช้า หลังอาหาร", "")
                    before_lunch = meal_times.get("มื้อเที่ยง ก่อนอาหาร", "")
                    after_lunch = meal_times.get("มื้อเที่ยง หลังอาหาร", "")
                    before_dinner = meal_times.get("มื้อเย็น ก่อนอาหาร", "")
                    after_dinner = meal_times.get("มื้อเย็น หลังอาหาร", "")
                    before_sleep = meal_times.get("มื้อก่อนนอน", "")
                    
                    time_flags = {
                        "before_breakfast_time": False,
                        "after_breakfast_time": False,
                        "before_lunch_time": False,
                        "after_lunch_time": False,
                        "before_dinner_time": False,
                        "after_dinner_time": False,
                        "before_sleep_time": False
                    }
                    
                    if not before_breakfast == "":
                        before_breakfast_seconds = time_to_seconds(before_breakfast)
                        before_breakfast_time = True
                        time_flags["before_breakfast_time"] = True
                    if not after_breakfast == "":    
                        after_breakfast_seconds = time_to_seconds(after_breakfast)
                        after_breakfast_time = True
                        time_flags["after_breakfast_time"] = True
                    if not before_lunch == "":
                        before_lunch_seconds = time_to_seconds(before_lunch)
                        before_lunch_time = True
                        time_flags["before_lunch_time"] = True
                    if not after_lunch == "":
                        after_lunch_seconds = time_to_seconds(after_lunch)
                        after_lunch_time = True
                        time_flags["after_lunch_time"] = True
                    if not before_dinner == "":
                        before_dinner_seconds = time_to_seconds(before_dinner)
                        before_dinner_time = True
                        time_flags["before_dinner_time"] = True
                    if not after_dinner == "":
                        after_dinner_seconds = time_to_seconds(after_dinner)
                        after_dinner_time = True
                        time_flags["after_dinner_time"] = True
                    if not before_sleep == "":
                        before_sleep_seconds = time_to_seconds(before_sleep)
                        before_sleep_time = True
                        time_flags["before_sleep_time"] = True
            
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    
                    if current_time == cur_meal_time:                           # แก้ cur_meal_time
                        meal_seconds = time_to_seconds(current_time)
                        self.meal_seconds = time_to_seconds(current_time)           # meal_seconds เวอร์ชัน update time
                        col, row, servoNum = self.load_state()
                        while row < self.max_row:
                            while col < self.max_col:
                                
                                # self.pwm.set_pwm(servoNum, 0, self.servo_max)      
                                # self.pwm.set_pwm(servoNum + 1, 0, self.servo_max)
                                
                                cur_col, cur_row, servoNum = self.load_state()
                                
                                for check_col, check_row, drug_id, drug_name, meal_id, meal_name, meal_time, state in meal_drug_list:
                                    if check_col == cur_col and check_row == cur_row:
                                        selected_items.append((check_col, check_row, drug_id, drug_name, meal_id, meal_name, meal_time))
                                
                                cur_meal_name = selected_items[-1][5]
                                cur_meal_time = meal_times.get(f"{cur_meal_name}", "")
                                
                                meal_times = self.load_meal_times_from_database()
            
                                # เข้าถึง meal times โดยใช้ชื่อมื้อ
                                before_breakfast = meal_times.get("มื้อเช้า ก่อนอาหาร", "")
                                after_breakfast = meal_times.get("มื้อเช้า หลังอาหาร", "")
                                before_lunch = meal_times.get("มื้อเที่ยง ก่อนอาหาร", "")
                                after_lunch = meal_times.get("มื้อเที่ยง หลังอาหาร", "")
                                before_dinner = meal_times.get("มื้อเย็น ก่อนอาหาร", "")
                                after_dinner = meal_times.get("มื้อเย็น หลังอาหาร", "")
                                before_sleep = meal_times.get("มื้อก่อนนอน", "")
                                
                                if not before_breakfast == "":
                                    before_breakfast_seconds = time_to_seconds(before_breakfast)
                                    before_breakfast_time = True
                                    time_flags["before_breakfast_time"] = True
                                if not after_breakfast == "":    
                                    after_breakfast_seconds = time_to_seconds(after_breakfast)
                                    after_breakfast_time = True
                                    time_flags["after_breakfast_time"] = True
                                if not before_lunch == "":
                                    before_lunch_seconds = time_to_seconds(before_lunch)
                                    before_lunch_time = True
                                    time_flags["before_lunch_time"] = True
                                if not after_lunch == "":
                                    after_lunch_seconds = time_to_seconds(after_lunch)
                                    after_lunch_time = True
                                    time_flags["after_lunch_time"] = True
                                if not before_dinner == "":
                                    before_dinner_seconds = time_to_seconds(before_dinner)
                                    before_dinner_time = True
                                    time_flags["before_dinner_time"] = True
                                if not after_dinner == "":
                                    after_dinner_seconds = time_to_seconds(after_dinner)
                                    after_dinner_time = True
                                    time_flags["after_dinner_time"] = True
                                if not before_sleep == "":
                                    before_sleep_seconds = time_to_seconds(before_sleep)
                                    before_sleep_time = True
                                    time_flags["before_sleep_time"] = True
                                
                                true_count = sum(time_flags.values())
                                
                                now = datetime.now()
                                current_time = now.strftime("%H:%M:%S")
                                
                                if current_time == cur_meal_time:
                                    self.save_notify_state(True)
                                    
                                    meal_seconds = time_to_seconds(current_time)
                                    self.meal_seconds = time_to_seconds(current_time)           # meal_seconds เวอร์ชัน update time
                                    self.pwm.set_pwm(servoNum + 1, 0, self.servo_min)         #เซอร์โวตัวหลัง
                                    time.sleep(1)
                                    self.pwm.set_pwm(servoNum + 1, 0, self.servo_max)         
                                    time.sleep(1)
                                    
                                    self.pwm.set_pwm(servoNum, 0, self.servo_min)             #เซอร์โวตัวหน้า
                                    time.sleep(1)
                                    self.pwm.set_pwm(servoNum, 0, self.servo_max)
                                    time.sleep(1)
                                    
                                    self.pwm.set_pwm(servoNum + 1, 0, self.servo_max)
                                    time.sleep(1)
                                    
                                    connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/db/medicine.db")
                                    cursor = connection.cursor()
                                                                    
                                    for check_col, check_row, drug_id, drug_name, meal_id, meal_name, meal_time, state in meal_drug_list:
                                        # print(f"{check_row} == {cur_row}")
                                        # print(f"{check_col} == {cur_col}")
                                        # print("----------------")
                                        if check_row == cur_row and check_col == cur_col:
                                            query = f'''
                                                SELECT drug_remaining, drug_remaining_meal, internal_drug, drug_eat
                                                    FROM Drug
                                                    WHERE drug_id = {drug_id}
                                                '''
                                            cursor.execute(query)
                                            drug_info_list = cursor.fetchall()
                                            print("drug_info_list")
                                            if drug_info_list:
                                                drug_remaining, drug_remaining_meal, internal_drug, drug_eat = drug_info_list[0]
                                                internal_drug -= 1
                                                drug_remaining -= drug_eat
                                                drug_remaining_meal = drug_remaining / drug_eat
                                                update_query = f'''
                                                    UPDATE Drug
                                                    SET drug_remaining = {drug_remaining},
                                                        drug_remaining_meal = {drug_remaining_meal},
                                                        internal_drug = {internal_drug}
                                                    WHERE drug_id = {drug_id}
                                                    '''
                                                cursor.execute(update_query)
                                                connection.commit()
                                                
                                    col += 1
                                    
                                    for i, item in enumerate(meal_drug_list):
                                        if item[0] == cur_col and item[1] == cur_row:
                                            meal_drug_list[i] = (item[0], item[1], item[2], item[3], item[4], item[5], item[6], 1)
                                    self.save_meal_drug_list(meal_drug_list)
                                    ####################################################################################                        
                                    
                                    if current_time == before_breakfast:
                                        meal_name = "มื้อเช้า ก่อนอาหาร"
                                    elif current_time == after_breakfast:
                                        meal_name = "มื้อเช้า หลังอาหาร"
                                    elif current_time == before_lunch:
                                        meal_name = "มื้อเที่ยง ก่อนอาหาร"
                                    elif current_time == after_lunch:
                                        meal_name = "มื้อเที่ยง หลังอาหาร"
                                    elif current_time == before_dinner:
                                        meal_name = "มื้อเย็น ก่อนอาหาร"
                                    elif current_time == after_dinner:
                                        meal_name = "มื้อเย็น หลังอาหาร"
                                    elif current_time == before_sleep:
                                        meal_name = "มื้อก่อนนอน"
                                        
                                    self.get_drug_line(self.channel_access_token, meal_name)            # รับยา
                                    self.get_drug()
                                    
                                    if bb_not_receive:
                                        print("ท่านลืมกินยามื้อ (เช้าก่อนอาหาร) ยาที่ลืมอยู่ในบอลสี (แดง) ในช่อง ยาลืมกิน")     #1
                                        bb_not_receive = False
                                        self.fg_bb()
                                    elif ab_not_receive:
                                        print("ท่านลืมกินยามื้อ (เช้าหลังอาหาร) ยาที่ลืมอยู่ในบอลสี (ส้ม) ในช่อง ยาลืมกิน")      #2
                                        ab_not_receive = False
                                        self.fg_ab()
                                    elif bl_not_receive:
                                        print("ท่านลืมกินยามื้อ (เที่ยงก่อนอาหาร) ยาที่ลืมอยู่ในบอลสี (เหลือง) ในช่อง ยาลืมกิน")  #3
                                        bl_not_receive = False
                                        self.fg_bl()
                                    elif al_not_receive:
                                        print("ท่านลืมกินยามื้อ (เที่ยงหลังอาหาร) ยาที่ลืมอยู่ในบอลสี (เขียวอ่อน) ในช่อง ยาลืมกิน")    #4
                                        al_not_receive = False
                                        self.fg_al()
                                    elif bd_not_receive:
                                        print("ท่านลืมกินยามื้อ (เย็นก่อนอาหาร) ยาที่ลืมอยู่ในบอลสี (เขียวเข้ม) ในช่อง ยาลืมกิน")     #5
                                        bd_not_receive = False
                                        self.fg_bd()
                                    elif ad_not_receive:
                                        print("ท่านลืมกินยามื้อ (เย็นหลังอาหาร) ยาที่ลืมอยู่ในบอลสี (ฟ้า) ในช่อง ยาลืมกิน")      #6
                                        ad_not_receive = False
                                        self.fg_ad()
                                    elif bbed_not_receive:
                                        print("ท่านลืมกินยามื้อ (ก่อนนอน) ยาที่ลืมอยู่ในบอลสี (น้ำเงิน) ในช่อง ยาลืมกิน")     #7
                                        bbed_not_receive = False
                                        self.fg_ad()
                                    
                                    # Line
                                    start_time = time.time()            # เก็บเวลาเริ่มต้นเพื่อใช้ในการตรวจสอบระยะเวลา 5 นาที
                                    notify_time = 1                     # ตัวแปรเริ่มต้นแจ้งเตือนไลน์
                                    notify_second = 300                  # เวลาในการแจ้งเตือนที่จะเกิดในไลน์
                                    max_replay_notify = 4               # จำนวนการแจ้งเตือนไฟล์เสียงที่ไม่ได้รับประทานยา
                                    
                                    # ระยะจากคนและกล่องจ่ายยา (cm)
                                    range_user = 60                     # ระยะจากผู้ใช้กับตัวกล่องยา
                                    
                                    get_drug = False
                                    stay_in_loop = True
                                    while stay_in_loop:

                                        self.distance_event.set()
                                        
                                        self.motion_detect_event.set()         # เรียกฟังก์ชันตรวจจับการเคลื่อนไหว
                                        
                                        self.led_blink()
                                        
                                        if not get_drug:
                                            self.beep_event.set()                                                         
                                        
                                        if self.distance_value < range_user and GPIO.input(self.GPIO_PIR):          # ตรวจสอบระยะและใช้ Motion sensor ในการตรวจจับการเคลื่อนไหวที่มารับยา
                                            get_drug = True                                                                                               
                                        
                                        # เงื่อนไขการแจ้งเตือนซ้ำ
                                        if time.time() - start_time >= notify_second and notify_time != max_replay_notify:
                                            self.wait_receive_line(self.channel_access_token, notify_time)
                                            notify_time += 1
                                                                
                                            start_time = time.time()
                                        
                                        # print(f"self.meal_seconds --> {self.meal_seconds}")
                                        # print(f"after_breakfast_seconds --> {after_breakfast_seconds}")
                                        # print(f"self.meal_seconds >= after_breakfast_seconds - (5 * 60) --> {self.meal_seconds >= after_breakfast_seconds - (5 * 60)}")
                                        # print(f"self.meal_seconds <= after_breakfast_seconds --> {self.meal_seconds <= after_breakfast_seconds}")
                                        # print(f"meal_seconds != after_breakfast_seconds --> {meal_seconds != after_breakfast_seconds}")
                                        # print(f"after_breakfast_time --> {after_breakfast_time}")
                                        
                                        current_day = datetime.now().date()
                                        
                                        print(f"self.previous_day --> {self.previous_day}")
                                        print(f"current_day --> {current_day}")
                                        if current_day != self.previous_day:
                                            self.is_new_day = True
                                            self.previous_day = current_day
                                            
                                        ########################################################################################
                                        if true_count == 1:
                                            if self.meal_seconds >= before_breakfast_seconds - (5 * 60) and before_breakfast_time and self.is_new_day:
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                bb_not_receive = True                     
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                                
                                                if self.is_new_day:
                                                    self.is_new_day = False
                                            
                                            elif self.meal_seconds >= after_breakfast_seconds - (5 * 60) and after_breakfast_time and self.is_new_day:
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                ab_not_receive = True                     
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                                
                                                if self.is_new_day:
                                                    self.is_new_day = False
                                                
                                            elif self.meal_seconds >= before_lunch_seconds - (5 * 60) and before_lunch_time and self.is_new_day:
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                bl_not_receive = True                     
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                                
                                                if self.is_new_day:
                                                    self.is_new_day = False
                                                
                                            elif self.meal_seconds >= after_lunch_seconds - (5 * 60) and after_lunch_time and self.is_new_day:
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                al_not_receive = True                     
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                                
                                                if self.is_new_day:
                                                    self.is_new_day = False
                                                
                                            elif self.meal_seconds >= before_dinner_seconds - (5 * 60) and before_dinner_time and self.is_new_day:
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                bd_not_receive = True                     
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                                
                                                if self.is_new_day:
                                                    self.is_new_day = False
                                                
                                            elif self.meal_seconds >= after_dinner_seconds - (5 * 60) and after_dinner_time and self.is_new_day:
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                ad_not_receive = True                     
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                                
                                                if self.is_new_day:
                                                    self.is_new_day = False
                                                
                                            elif self.meal_seconds >= before_sleep_seconds - (5 * 60) and before_sleep_time and self.is_new_day:
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                bbed_not_receive = True                     
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                                
                                                if self.is_new_day:
                                                    self.is_new_day = False
                                                
                                        ##########################################################################################        
                                        else:
                                            if self.meal_seconds >= before_breakfast_seconds - (5 * 60) and self.meal_seconds <= before_breakfast_seconds and meal_seconds != before_breakfast_seconds and before_breakfast_time:
                                                
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                bbed_not_receive = True                     
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                            elif self.meal_seconds >= after_breakfast_seconds - (5 * 60) and self.meal_seconds <= after_breakfast_seconds and meal_seconds != after_breakfast_seconds and after_breakfast_time:
                                                
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                bb_not_receive = True                            
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                            elif self.meal_seconds >= before_lunch_seconds - (5 * 60) and self.meal_seconds <= before_lunch_seconds and meal_seconds != before_lunch_seconds and before_lunch_time:
                                                
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                ab_not_receive = True                                  
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                            elif self.meal_seconds >= after_lunch_seconds - (5 * 60) and self.meal_seconds <= after_lunch_seconds and meal_seconds != after_lunch_seconds and after_lunch_time:
                                                
                                                
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)  
                                                bl_not_receive = True                               
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                            elif self.meal_seconds >= before_dinner_seconds - (5 * 60) and self.meal_seconds <= before_dinner_seconds and meal_seconds != before_dinner_seconds and before_dinner_time:
                                                
                                                
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                al_not_receive = True                                 
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                            elif self.meal_seconds >= after_dinner_seconds - (5 * 60) and self.meal_seconds <= after_dinner_seconds and meal_seconds != after_dinner_seconds and after_dinner_time:
                                                
                                                
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name)
                                                bd_not_receive = True                                 
                                                stay_in_loop = False
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                
                                                self.save_main_state(True)
                                            elif self.meal_seconds >= before_sleep_seconds - (5 * 60) and self.meal_seconds <= before_sleep_seconds and meal_seconds != before_sleep_seconds and before_sleep_time:
                                                print(f"ผู้สูงอายุไม่มารับยา {meal_name}")
                                                notify_time = 1
                                                self.pwm.set_pwm(15, 0, self.servo_drop)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                                time.sleep(2)
                                                self.pwm.set_pwm(15, 0, self.servo_max)
                                                time.sleep(1)
                                                self.not_receive_line(self.channel_access_token, meal_name) 
                                                bd_not_receive = True       
                                                
                                                self.distance_event.clear()
                                                self.motion_detect_event.clear()
                                                self.beep_event.clear()
                                                                        
                                                stay_in_loop = False
                                                self.save_main_state(True)
                                        # เงื่อนไขถ้ามารับยา
                                        if get_drug:
                                            print("ผู้สูงอายุมารับยาแล้ว")       
                                            
                                            self.distance_event.clear()
                                            self.motion_detect_event.clear()
                                            self.beep_event.clear()
                                                                                                                
                                            capture_image_thread = threading.Thread(target=self.capture_image)
                                            capture_image_thread.start()
                                            capture_image_thread.join()
                                        
                                            self.send_image_to_line(self.image_url, self.channel_access_token, meal_name)               
                                            
                                            stay_in_loop = False
                                            self.save_main_state(True)
                                            
                                            # print(meal_drug_list[-1][0])
                                            # print(meal_drug_list[-1][1])
                                        
                                        if not col == self.max_col:    
                                            if cur_col != meal_drug_list[-1][0] or cur_row != meal_drug_list[-1][1]:
                                                self.save_state(col, row, servoNum)  # Save the current state
                                                # print("h")   
                                            
                                            if cur_col == meal_drug_list[-1][0] and cur_row == meal_drug_list[-1][1]:     
                                                self.save_state(0,0,0)
                                                self.save_prepare_state(False)
                                                print("e")
                                                self.all_drug_empty = True
                                
                                if self.all_drug_empty:
                                    break
                                                
                            # เพิ่มเงื่อนไขที่ถ้า col = 3 ให้กลับไปที่ 0
                            if col == self.max_col:
                                col = 0
                                                
                            row += 1
                            servoNum += 2               # จำนวนเซอร์โว 2 ตัว และไปแถวถัดไป      
                            
                            if not row == self.max_row:
                                if cur_col != meal_drug_list[-1][0] or cur_row != meal_drug_list[-1][1]:
                                    self.save_state(col, row, servoNum)  # Save the current state
                                    print("l")
                                
                                elif cur_col == meal_drug_list[-1][0] and cur_row == meal_drug_list[-1][1]:
                                    self.save_state(0,0,0)
                                    self.save_prepare_state(False)
                                    print("ll")
                            
                        row = 0
                        servoNum = 0
                        
                        if cur_col != meal_drug_list[-1][0] or cur_row != meal_drug_list[-1][1]:
                            self.save_state(col, row, servoNum)  # Save the current state
                            print("o")
                        
                        if cur_col == meal_drug_list[-1][0] and cur_row == meal_drug_list[-1][1]:
                            self.save_state(0,0,0)
                            self.save_prepare_state(False)
                            print("!")
        
        except KeyboardInterrupt:
            print("\nถูกหยุดการทำงานโดยผู้ใช้")
            GPIO.cleanup()                
    
            
    def stop(self):
        self.is_running = False
        self.finished.emit()
        print("-------------finish-------------")
        
    def run_thread(self):
        self.thread = QThread()
        self.sensor_thread = SensorThread()  
        self.sensor_thread.moveToThread(self.thread)
        self.thread.started.connect(self.sensor_thread.run)
        self.sensor_thread.finished.connect(self.thread.quit)   
        self.thread.start()
