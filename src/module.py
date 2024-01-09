from __future__ import division

from Utils import *
from UI_Generate import *

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QGraphicsDropShadowEffect, QLabel
from PyQt5.QtCore import QThread, pyqtSignal, QObject, QTimer, QLocale

import sys
import time
import RPi.GPIO as GPIO

from datetime import datetime
import os
import Adafruit_PCA9685
import subprocess
import threading
# from playsound import playsound
import requests
import pygame

from drug_List import Ui_drug_List
from select_time import Ui_select_time
# from pack_med import Ui_med_pack
from pack import Ui_med_pack
from sortDrug import Ui_sortDrug
from drugTotal import Ui_drugTotal
from wifi import Ui_wifi

import sqlite3

########################### Thread ###########################
class SensorThread(QObject):
    finished = pyqtSignal()
    
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
        
        # self.pwm = Adafruit_PCA9685.PCA9685()
        self.servo_min = 90
        self.servo_max = 570
        self.max_col = 2
        self.max_row = 5
        
        self.state_file = 'servo_state.txt'
        
        # Set frequency to 60hz, good for servos.
        # self.pwm.set_pwm_freq(60)
        
    ####################### สำหรับ Ultrasonic Sensor ########################

    def distance(self):
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
        distance = (TimeElapsed * 34300) / 2
    
        return distance

    ########################################################################

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
                print(f'Loaded state: {state[0]},{state[1]},{state[2]}')
                return state
        return 0, 0, 0  # default values if the file doesn't exist


    # Helper function to make setting a servo pulse width simpler.
    # def set_servo_pulse(self, channel, pulse):
    #     pulse_length = 1000000    # 1,000,000 us per second
    #     pulse_length //= 60       # 60 Hz
    #     print('{0}us per period'.format(pulse_length))
    #     pulse_length //= 4096     # 12 bits of resolution
    #     print('{0}us per bit'.format(pulse_length))
    #     pulse *= 1000
    #     pulse //= pulse_length
    #     self.pwm.set_pwm(channel, 0, pulse)



    ############################# สำหรับ Audio ##############################

    def get_drug(self):
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/get_drug.mp3")
        pygame.mixer.music.play()
        # time.sleep(3)

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    def beep_audio(self):
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

    def fg_bb(self):
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Set the duration to 1 minute (60,000 milliseconds)

        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Documents/Medicine_notify/sound/fg_bb.mp3")
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

    ########################## สำหรับ PIR Sensor ############################

    def motion_detect(self):
        # print("Waiting for sensor to settle")

        if GPIO.input(self.GPIO_PIR):              # Check whether pir is HIGH
            print("Motion Detected!")
        else:
            print("No Motion Detected!")
            # pass


    ############################ LED #######################################

    def led_blink(self):
        # Toggle the LED based on the current time
        GPIO.output(self.led_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(self.led_pin, GPIO.LOW)
        time.sleep(0.5)
        
    ##################### สำหรับ Line Messaging API #########################

    def get_drug_line(self, channel_access_token, meal_name):
        url = "https://api.line.me/v2/bot/message/push"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + channel_access_token,
        }

        data = {
            "to": "Ub6246111505735410a4409ab3601a7f1",
            "messages": [
                {
                    "type": "text",
                    "text": f"ถึงเวลารับประทานยา {meal_name}"
                }
            ],
        }
        
        response = requests.post(url, json=data, headers=headers)
        print(response.text)
    
    # ส่งรูปภาพเมื่อมารับยา
    def send_image_to_line(self, image_url, channel_access_token, meal_name):
        url = "https://api.line.me/v2/bot/message/push"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + channel_access_token,
        }

        data = {
            "to": "Ub6246111505735410a4409ab3601a7f1",
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

        response = requests.post(url, json=data, headers=headers)
        print(response.text)
        
    def not_receive_line(self, channel_access_token, meal_name):
        url = "https://api.line.me/v2/bot/message/push"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + channel_access_token,
        }

        data = {
            "to": "Ub6246111505735410a4409ab3601a7f1",
            "messages": [
                {
                    "type": "text",
                    "text": f"ผู้สูงอายุไม่ได้มารับยา{meal_name}"
                }
            ],
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.text)
        
    def wait_receive_line(self, channel_access_token, number):
        url = "https://api.line.me/v2/bot/message/push"
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + channel_access_token,
        }

        data = {
            "to": "Ub6246111505735410a4409ab3601a7f1",
            "messages": [
                {
                    "type": "text",
                    "text": f"แจ้งเตือนครั้งที่ {number} ผู้สูงอายุยังไม่มารับยาใน {number*5} นาทีนี้",
                }
            ],
        }

        response = requests.post(url, json=data, headers=headers)
        print(response.text)
        
    #################### ส่ง request ให้ header ##############################

    def send_request_with_header(self, url, header_name, header_value):
        headers = {header_name: header_value}
        response = requests.get(url, headers=headers)
    #     print(response.text)
        
    ########################################################################

    def load_meal_times_from_database(self):
        connection = sqlite3.connect("/home/pi/Documents/Medicine_notify/src/medicine.db")
        cursor = connection.cursor()

        cursor.execute("SELECT meal_name, time FROM Meal")
        drugs = cursor.fetchall()

        meal_times = dict(drugs)

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
        
        meal_times = self.load_meal_times_from_database()
        
        def update_meal_seconds():
            while True:
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                self.meal_seconds = time_to_seconds(current_time)

        update_thread = threading.Thread(target=update_meal_seconds)
        update_thread.start()
        
        # meal_times = self.load_meal_times_from_database()

        GPIO.output(self.led_pin, GPIO.LOW)
        
        bb_not_receive = False
        ab_not_receive = False
        bl_not_receive = False
        al_not_receive = False
        bd_not_receive = False
        ad_not_receive = False
        bbed_not_receive = False

        before_breakfast = "07:00:00"
        after_breakfast = "07:30:00"
        before_lunch = "12:00:00"
        after_lunch = "12:30:00"
        before_dinner = "18:00:00"
        after_dinner = "18:30:00"
        before_sleep = "21:00:00"
        
        before_breakfast_seconds = time_to_seconds(before_breakfast)
        after_breakfast_seconds = time_to_seconds(after_breakfast)
        before_lunch_seconds = time_to_seconds(before_lunch)
        after_lunch_seconds = time_to_seconds(after_lunch)
        before_dinner_seconds = time_to_seconds(before_dinner)
        after_dinner_seconds = time_to_seconds(after_dinner)
        before_sleep_seconds = time_to_seconds(before_sleep)

        # แสดงผลลัพธ์
        # print(f"Before Breakfast: {before_breakfast_seconds} seconds")
        # print(f"After Breakfast: {after_breakfast_seconds} seconds")
        # print(f"Before Lunch: {before_lunch_seconds} seconds")
        # print(f"After Lunch: {after_lunch_seconds} seconds")
        # print(f"Before Dinner: {before_dinner_seconds} seconds")
        # print(f"After Dinner: {after_dinner_seconds} seconds")
        # print(f"Before Sleep: {before_sleep_seconds} seconds")

        # # Access meal times using the meal names
        # before_breakfast = meal_times.get("มื้อเช้า ก่อนอาหาร", "")
        # after_breakfast = meal_times.get("มื้อเช้า หลังอาหาร", "")
        # before_lunch = meal_times.get("มื้อเที่ยง ก่อนอาหาร", "")
        # after_lunch = meal_times.get("มื้อเที่ยง หลังอาหาร", "")
        # before_dinner = meal_times.get("มื้อเย็น ก่อนอาหาร", "")
        # after_dinner = meal_times.get("มื้อเย็น หลังอาหาร", "")
        # before_sleep = meal_times.get("มื้อก่อนนอน", "")
        
        # รัน Process แบบ Multiprocessing    
        web_server_thread = threading.Thread(target=self.server)
        # รัน web_server
        web_server_thread.start()

        # Channel Access Token และ URL ของไฟล์สำหรับเก็บรูปภาพใน Line
        self.ngrok_url = 'https://secure-zebra-lately.ngrok-free.app/'
        self.image_url = "https://secure-zebra-lately.ngrok-free.app/image.jpg"
        self.channel_access_token = "o776VQ6aRKQlMK0EbeahQt0AmQAvY8RLv0L5fDGgPqhiccGJZnCa/Efir1W4tdsN03TLojY+CEHcM8sk97XJTc+URIvZLw9IRZvRHPYQmZvnZl65E5Zy2dA5H7m+pkostxNs1Zxlg1Nzwe8CFM3s7wdB04t89/1O/w1cDnyilFU="

        # self.send_request_with_header(self.ngrok_url, 'ngrok-skip-browser-warning', 'true')       # ให้ skip หน้าเว็บ warning
        
        try:
            while True:
            
                # Move servo on channel O between extremes.
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_day = now.strftime("%A")  # Get the current day of the week
                # print(f"ขณะนี้เวลา: {current_time}, วัน: {current_day}")
                
                if current_time in [before_breakfast, after_breakfast, before_lunch, after_lunch, before_dinner, after_dinner, before_sleep]:
                    meal_seconds = time_to_seconds(current_time)
                    self.meal_seconds = time_to_seconds(current_time)           # meal_seconds เวอร์ชัน update time
                    col, row, servoNum = self.load_state()
                    while row < self.max_row:
                        while col < self.max_col:  
                            now = datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            current_day = now.strftime("%A")  # Get the current day of the week
                            # print(f"ขณะนี้เวลา: {current_time}, วัน: {current_day}")
                            
                            if current_time in [before_breakfast, after_breakfast, before_lunch, after_lunch, before_dinner, after_dinner, before_sleep]:
                                meal_seconds = time_to_seconds(current_time)
                                self.meal_seconds = time_to_seconds(current_time)           # meal_seconds เวอร์ชัน update time
                                # self.pwm.set_pwm(servoNum + 1, 0, self.servo_min)         #เซอร์โวตัวหลัง
                                # time.sleep(2)
                                
                                # self.pwm.set_pwm(servoNum, 0, self.servo_min)             #เซอร์โวตัวหน้า
                                # time.sleep(2)
                                # self.pwm.set_pwm(servoNum, 0, self.servo_max)
                                # time.sleep(1)
                                
                                # self.pwm.set_pwm(servoNum + 1, 0, self.servo_max)
                                # time.sleep(2)
                                                                    
                                col += 1
                                
                                if current_time == before_breakfast:
                                    meal_name = "มื้อเช้า ก่อนอาหาร"
                                elif current_time == after_breakfast:
                                    meal_name = "มื้อเช้า หลังอาหาร"
                                elif current_time == before_lunch:
                                    meal_name = "มื้อเช้า หลังอาหาร"
                                elif current_time == after_lunch:
                                    meal_name = "มื้อเช้า หลังอาหาร"
                                elif current_time == before_dinner:
                                    meal_name = "มื้อเช้า หลังอาหาร"
                                elif current_time == after_dinner:
                                    meal_name = "มื้อเช้า หลังอาหาร"
                                elif current_time == before_sleep:
                                    meal_name = "มื้อเช้า หลังอาหาร"
                                    
                                self.get_drug_line(self.channel_access_token, meal_name)            # รับยา
                                self.get_drug()
                                
                                if bb_not_receive:
                                    print("ท่านลืมกินยามื้อ (เช้าก่อนอาหาร) ยาที่ลืมอยู่ในบอลสี (แดง) ในช่อง ยาลืมกิน")     #2
                                    bb_not_receive = False
                                    self.fg_bb()
                                elif ab_not_receive:
                                    print("ท่านลืมกินยามื้อ (เช้าหลังอาหาร) ยาที่ลืมอยู่ในบอลสี (ส้ม) ในช่อง ยาลืมกิน")      #3
                                    time.sleep(10)
                                    ab_not_receive = False
                                    self.fg_ab()
                                elif bl_not_receive:
                                    print("ท่านลืมกินยามื้อ (เที่ยงก่อนอาหาร) ยาที่ลืมอยู่ในบอลสี (เหลือง) ในช่อง ยาลืมกิน")  #4
                                    time.sleep(10)
                                    bl_not_receive = False
                                    self.fg_bl()
                                elif al_not_receive:
                                    print("ท่านลืมกินยามื้อ (เที่ยงหลังอาหาร) ยาที่ลืมอยู่ในบอลสี (เขียวอ่อน) ในช่อง ยาลืมกิน")    #5
                                    time.sleep(10)
                                    al_not_receive = False
                                    self.fg_al()
                                elif bd_not_receive:
                                    print("ท่านลืมกินยามื้อ (เย็นก่อนอาหาร) ยาที่ลืมอยู่ในบอลสี (เขียวเข้ม) ในช่อง ยาลืมกิน")     #6
                                    bd_not_receive = False
                                    self.fg_bd()
                                elif ad_not_receive:
                                    print("ท่านลืมกินยามื้อ (เย็นหลังอาหาร) ยาที่ลืมอยู่ในบอลสี (ฟ้า) ในช่อง ยาลืมกิน")      #7
                                    ad_not_receive = False
                                    self.fg_ad()
                                elif bbed_not_receive:
                                    print("ท่านลืมกินยามื้อ (ก่อนนอน) ยาที่ลืมอยู่ในบอลสี (น้ำเงิน) ในช่อง ยาลืมกิน")     #8
                                    bbed_not_receive = False
                                    self.fg_ad()
                                
                                # Line
                                start_time = time.time()            # เก็บเวลาเริ่มต้นเพื่อใช้ในการตรวจสอบระยะเวลา 5 นาที
                                notify_time = 1                     # จำนวนครั้งการแจ้งเตือนไลน์
                                notify_second = 300                  # เวลาในการแจ้งเตือนที่จะเกิดในไลน์
                                max_replay_notify = 4               # จำนวนการแจ้งเตือนไฟล์เสียงที่ไม่ได้รับประทานยา
                                
                                # ไฟล์เสียง beep
                                audio_time = time.time()            # เก็บเวลาเริ่มต้นเพื่อใช้ในการตรวจสอบระยะการเล่นไฟล์เสียง
                                audio_play = 3                      # เล่นไฟล์ใน 3 วินาที
                                
                                # ระยะจากคนและกล่องจ่ายยา (cm)
                                range_user = 50                     # ระยะจากผู้ใช้กับตัวกล่องยา
                                
                                
                                get_drug = False
                                stay_in_loop = True
                                while stay_in_loop:           
                                    dist1 = self.distance()
                                    time.sleep(0.005)
                                    # dist2 = self.distance()
                                    # time.sleep(0.005)
                                    
                                    print ("Measured Distance = %.1f cm" % dist1)
                                    # print ("Measured Distance 2 = %.1f cm" % dist2)
                                    self.motion_detect()         # เรียกฟังก์ชันตรวจจับการเคลื่อนไหว
                                    
                                    
                                    # self.led_blink()
                                    self.led_blink()
                                    
                                    # if time.time() - start_led_time <= led_play and not get_drug:
                                        
                                    #     start_led_time = time.time()
                                        
                                    
                                    # if not beep_process.is_alive() and time.time() - audio_time >= audio_play and not get_drug:
                                    if time.time() - audio_time >= audio_play and not get_drug:
                                        # beep_process = multiprocessing.Process(target=self.beep)
                                        print("beep ~ beep")
                                        # beep_process.start()        #9
                                        self.beep_audio()
                                        
                                        # start_led_time = time.time()
                                        audio_time = time.time()
                                        
                                    
                                    # if dist1 < range_user and dist2 < range_user and GPIO.input(self.GPIO_PIR):          # ตรวจสอบระยะที่ 1 และ 2 เปรียบเทียบเพื่อป้องกันความผิดพลาดของเซนเซอร์ 
                                    #     get_drug = True                                                          # และใช้ Motion sensor ในการตรวจจับการเคลื่อนไหวที่มารับยา
                                    
                                    if dist1 < range_user and GPIO.input(self.GPIO_PIR):          # ตรวจสอบระยะที่ 1 และ 2 เปรียบเทียบเพื่อป้องกันความผิดพลาดของเซนเซอร์ 
                                        get_drug = True                                                          # และใช้ Motion sensor ในการตรวจจับการเคลื่อนไหวที่มารับยา                                    
                                    
                                    # เงื่อนไขการแจ้งเตือนซ้ำ
                                    if time.time() - start_time >= notify_second and notify_time != max_replay_notify:
                                        print(time.time)
                                        print(start_time)
                                        self.wait_receive_line(self.channel_access_token, notify_time)
                                        notify_time += 1
                                                            
                                        start_time = time.time()
                                    
                                    # เงื่อนไขไม่มารีบยา
                                    # if time.time() - start_time >= notify_second and notify_time == max_replay_notify:
                                    
                                    # print(self.meal_seconds)
                                    # print(meal_seconds)
                                    # print(before_breakfast_seconds)
                                    # print(after_breakfast_seconds)
                                    
                                    # if current_time >= after_breakfast_seconds - (5 * 60) and current_time <= after_breakfast_seconds and current_time_tmp != after_breakfast_seconds:
                                    
                                    if self.meal_seconds >= before_breakfast_seconds - (5 * 60) and self.meal_seconds <= before_breakfast_seconds and meal_seconds != before_breakfast_seconds:
                                        time.sleep(3)
                                        print("ผู้สูงอายุไม่มารับยา มื้อก่อนนอน")
                                        notify_time = 1
                                        # self.pwm.set_pwm(15, 0, self.servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                        # time.sleep(2)
                                        # self.pwm.set_pwm(15, 0, self.servo_max)
                                        # time.sleep(1)
                                        bbed_meal_name = "มื้อก่อนนอน"
                                        self.not_receive_line(self.channel_access_token, bbed_meal_name)
                                        bbed_not_receive = True                     
                                        stay_in_loop = False
                                        # break
                                    elif self.meal_seconds >= after_breakfast_seconds - (5 * 60) and self.meal_seconds <= after_breakfast_seconds and meal_seconds != after_breakfast_seconds:
                                        time.sleep(3)
                                        print("ผู้สูงอายุไม่มารับยา มื้อเช้า ก่อนอาหาร")
                                        notify_time = 1
                                        # self.pwm.set_pwm(15, 0, self.servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                        # time.sleep(2)
                                        # self.pwm.set_pwm(15, 0, self.servo_max)
                                        # time.sleep(1)
                                        bb_meal_name = "มื้อเช้า ก่อนอาหาร"
                                        self.not_receive_line(self.channel_access_token, bb_meal_name)
                                        bb_not_receive = True                            
                                        stay_in_loop = False
                                        # break
                                    elif self.meal_seconds >= before_lunch_seconds - (5 * 60) and self.meal_seconds <= before_lunch_seconds and meal_seconds != before_lunch_seconds:
                                        time.sleep(3)
                                        print("ผู้สูงอายุไม่มารับยา มื้อเช้า หลังอาหาร")
                                        notify_time = 1
                                        # self.pwm.set_pwm(15, 0, self.servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                        # time.sleep(2)
                                        # self.pwm.set_pwm(15, 0, self.servo_max)
                                        # time.sleep(1)
                                        ab_meal_name = "มื้อเช้า หลังอาหาร"
                                        self.not_receive_line(self.channel_access_token, ab_meal_name)
                                        ab_not_receive = True                                  
                                        stay_in_loop = False
                                        # break
                                    elif self.meal_seconds >= after_lunch_seconds - (5 * 60) and self.meal_seconds <= after_lunch_seconds and meal_seconds != after_lunch_seconds:
                                        
                                        time.sleep(3)
                                        print("ผู้สูงอายุไม่มารับยา มื้อเที่ยง ก่อนอาหาร")
                                        notify_time = 1
                                        # self.pwm.set_pwm(15, 0, self.servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                        # time.sleep(2)
                                        # self.pwm.set_pwm(15, 0, self.servo_max)
                                        # time.sleep(1)
                                        bl_meal_name = "มื้อเที่ยง ก่อนอาหาร"
                                        self.not_receive_line(self.channel_access_token, bl_meal_name)  
                                        bl_not_receive = True                               
                                        stay_in_loop = False
                                        # break
                                    elif self.meal_seconds >= before_dinner_seconds - (5 * 60) and self.meal_seconds <= before_dinner_seconds and meal_seconds != before_dinner_seconds:
                                        
                                        time.sleep(3)
                                        print("ผู้สูงอายุไม่มารับยา มื้อเที่ยง หลังอาหาร")
                                        notify_time = 1
                                        # self.pwm.set_pwm(15, 0, self.servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                        # time.sleep(2)
                                        # self.pwm.set_pwm(15, 0, self.servo_max)
                                        # time.sleep(1)
                                        al_meal_name = "มื้อเที่ยง หลังอาหาร"
                                        self.not_receive_line(self.channel_access_token, al_meal_name)
                                        al_not_receive = True                                 
                                        stay_in_loop = False
                                        # break
                                    elif self.meal_seconds >= after_dinner_seconds - (5 * 60) and self.meal_seconds <= after_dinner_seconds and meal_seconds != after_dinner_seconds:
                                        
                                        time.sleep(3)
                                        print("ผู้สูงอายุไม่มารับยา มื้อเย็น ก่อนอาหาร")
                                        notify_time = 1
                                        # self.pwm.set_pwm(15, 0, self.servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                        # time.sleep(2)
                                        # self.pwm.set_pwm(15, 0, self.servo_max)
                                        # time.sleep(1)
                                        bd_meal_name = "มื้อเย็น ก่อนอาหาร"
                                        self.not_receive_line(self.channel_access_token, bd_meal_name)
                                        bd_not_receive = True                                 
                                        stay_in_loop = False
                                        # break
                                    elif self.meal_seconds >= before_sleep_seconds - (5 * 60) and self.meal_seconds <= before_sleep_seconds and meal_seconds != before_sleep_seconds:
                                        
                                        time.sleep(3)
                                        print("ผู้สูงอายุไม่มารับยา มื้อเย็น หลังอาหาร")
                                        notify_time = 1
                                        # self.pwm.set_pwm(15, 0, self.servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                        # time.sleep(2)
                                        # self.pwm.set_pwm(15, 0, self.servo_max)
                                        # time.sleep(1)
                                        ad_meal_name = "มื้อเย็น หลังอาหาร"
                                        self.not_receive_line(self.channel_access_token, ad_meal_name) 
                                        bd_not_receive = True                             
                                        stay_in_loop = False
                                        # break
                                    # เงื่อนไขถ้ามารับยา
                                    if get_drug:
                                        print("ผู้สูงอายุมารับยาแล้ว")                                                                        
                                        capture_image_thread = threading.Thread(target=self.capture_image)
                                        capture_image_thread.start()
                                        capture_image_thread.join()
                                        
                                        if current_time == before_breakfast:
                                            meal_name = "มื้อเช้า ก่อนอาหาร"
                                        elif current_time == after_breakfast:
                                            meal_name = "มื้อเช้า หลังอาหาร"
                                        elif current_time == before_lunch:
                                            meal_name = "มื้อเช้า หลังอาหาร"
                                        elif current_time == after_lunch:
                                            meal_name = "มื้อเช้า หลังอาหาร"
                                        elif current_time == before_dinner:
                                            meal_name = "มื้อเช้า หลังอาหาร"
                                        elif current_time == after_dinner:
                                            meal_name = "มื้อเช้า หลังอาหาร"
                                        elif current_time == before_sleep:
                                            meal_name = "มื้อเช้า หลังอาหาร"
                                        
                                        
                                        self.send_image_to_line(self.image_url, self.channel_access_token, meal_name)               
                                        
                                        stay_in_loop = False
                                        # break
                                    
                                    if not col == self.max_col:
                                        self.save_state(col, row, servoNum)  # Save the current state       
                                
                        # เพิ่มเงื่อนไขที่ถ้า col = 3 ให้กลับไปที่ 0
                        if col == self.max_col:
                            col = 0
                                            
                        row += 1
                        servoNum += 2               # จำนวนเซอร์โว 2 ตัว และไปแถวถัดไป
                        
                        if not row == self.max_row:
                            self.save_state(col, row, servoNum)  # Save the current state
                        
                    row = 0
                    servoNum = 0
                    self.save_state(col, row, servoNum)  # Save the current state
                      
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
        
        # self.thread.started.connect(self.sensor_thread.receiveParams)
            
        self.sensor_thread.finished.connect(self.thread.quit)
        # self.sensor_thread.finished.connect(self.sensor_thread.deleteLater)
        # self.thread.finished.connect(self.thread.deleteLater)    
        self.thread.start()