# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
from datetime import datetime
import os
import time
import pygame
import RPi.GPIO as GPIO
import subprocess
import multiprocessing
import requests
import sqlite3
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

class MedicineDispenser:
    def __init__(self):
        #GPIO Mode (BOARD / BCM)
        GPIO.setmode(GPIO.BCM)

        #set GPIO Pins Ultrasonic Sensor
        self.GPIO_TRIGGER = 18 
        self.GPIO_ECHO = 24

        #set GPIO Pins Motion Sensor
        self.GPIO_PIR = 23

        # #et GPIO Pins LED
        self.led_pin = 16

        #set GPIO direction (IN / OUT)
        GPIO.setup(self.GPIO_TRIGGER, GPIO.OUT)
        GPIO.setup(self.GPIO_ECHO, GPIO.IN)
        GPIO.setup(self.GPIO_PIR, GPIO.IN)
        GPIO.setup(self.led_pin, GPIO.OUT)
        
        self.pwm = Adafruit_PCA9685.PCA9685()
        self.servo_min = 150
        self.servo_max = 600
        self.max_col = 2
        self.max_row = 2
        self.state_file = 'servo_state.txt'
        
        # Set frequency to 60hz, good for servos.
        self.pwm.set_pwm_freq(60)
        
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

    def save_state(self, row, col, servoNum):
        with open(self.state_file, 'w') as f:
            f.write(f'{row},{col},{servoNum}')

    def load_state(self):
        if os.path.exists(self.state_file):
            with open(self.state_file, 'r') as f:
                content = f.read().split(',')
                state = (int(content[0]), int(content[1]), int(content[2]))
                print(f'Loaded state: {state[0]},{state[1]},{state[2]}')
                return state
        return 0, 0, 0  # default values if the file doesn't exist


    # Helper function to make setting a servo pulse width simpler.
    def set_servo_pulse(self, channel, pulse):
        pulse_length = 1000000    # 1,000,000 us per second
        pulse_length //= 60       # 60 Hz
        print('{0}us per period'.format(pulse_length))
        pulse_length //= 4096     # 12 bits of resolution
        print('{0}us per bit'.format(pulse_length))
        pulse *= 1000
        pulse //= pulse_length
        self.pwm.set_pwm(channel, 0, pulse)



    ############################# สำหรับ Audio ##############################

    def play_recieve_drug_audio(self):
        # Initialize Pygame
        pygame.init()
        clock = pygame.time.Clock()

        # Print current time
        the_time = time.strftime("%H:%M:%S", time.localtime())
        print(the_time)

        # Play Sound
        print("ถึงเวลารับประทานยา")
        pygame.mixer.init()
        pygame.mixer.music.load("mario.mp3")
        pygame.mixer.music.play()

        # Wait for the sound to finish playing
        while pygame.mixer.music.get_busy():
            clock.tick(1)

        # Clean up Pygame
        pygame.mixer.quit()
        pygame.quit()
        
    def beep(self):
        subprocess.run(["python3", "/home/pi/Documents/Medicine_notify/src/beep.py"])

    # def beep_audio():
    #     # Initialize Pygame
    #     pygame.init()
    #     clock = pygame.time.Clock()

    #     # Set the duration to 1 minute (60,000 milliseconds)

    #     pygame.mixer.init()
    #     pygame.mixer.music.load("beep.mp3")
    #     pygame.mixer.music.play()
    #     time.sleep(3)

    #     # Wait for the sound to finish playing
    #     while pygame.mixer.music.get_busy():
    #         clock.tick(0.5)

    #     # Clean up Pygame
    #     pygame.mixer.quit()
    #     pygame.quit()

    ########################### สำหรับรัน Server #############################

    def server(self):
        subprocess.run(["./server.sh"])
        
    ############################# สำหรับถ่ายภาพ ##############################

    def capture_image(self):
        subprocess.run(["./capture_image.sh"])

    ########################## สำหรับ PIR Sensor ############################

    def motion_detect(self):
        # print("Waiting for sensor to settle")

        if GPIO.input(self.GPIO_PIR):              # Check whether pir is HIGH
            print("Motion Detected!")


    ############################ LED #######################################

    def led_blink(self):
        # Turn the LED on
        GPIO.output(self.led_pin, GPIO.HIGH)
        time.sleep(0.3)  # Pause for 1 second

        # Turn the LED off
        GPIO.output(self.led_pin, GPIO.LOW)
        time.sleep(0.3)  # Pause for 1 second

    # def led_blink():
    #     subprocess.run(["python3", "/home/pi/Documents/Medicine_notify/src/led_blink.py"])
        
    ##################### สำหรับ Line Messaging API #########################

    # ส่งรูปภาพเมื่อมารับยา
    def send_image_to_line(self, image_url, channel_access_token):
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
                    "text": "ผู้สูงอายุมารับยาแล้ว"
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
        
    def not_receive_line(self, channel_access_token):
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
                    "text": "ผู้สูงอายุไม่ได้มารับยา"
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
        
    ########################################################################

    def load_meal_times_from_database(self):
        connection = sqlite3.connect("medicine.db")
        cursor = connection.cursor()

        cursor.execute("SELECT meal_name, time FROM Meal")
        drugs = cursor.fetchall()

        meal_times = dict(drugs)

        connection.close()

        return meal_times

    def run(self):
        meal_times = self.load_meal_times_from_database()

        GPIO.output(self.led_pin, GPIO.LOW)

        before_breakfast = "11:33:00"
        after_breakfast = "02:02:30"
        before_lunch = "12:55:50"
        after_lunch = "12:56:00"
        before_dinner = "12:56:10"
        after_dinner = "12:56:20"
        before_sleep = "12:56:30"

        # # Access meal times using the meal names
        # before_breakfast = meal_times.get("มื้อเช้า ก่อนอาหาร", "")
        # after_breakfast = meal_times.get("มื้อเช้า หลังอาหาร", "")
        # before_lunch = meal_times.get("มื้อเที่ยง ก่อนอาหาร", "")
        # after_lunch = meal_times.get("มื้อเที่ยง หลังอาหาร", "")
        # before_dinner = meal_times.get("มื้อเย็น ก่อนอาหาร", "")
        # after_dinner = meal_times.get("มื้อเย็น หลังอาหาร", "")
        # before_sleep = meal_times.get("มื้อก่อนนอน", "")
            
        print('Moving servo on channel 0, press Ctrl-C to quit...')

        # รัน Process แบบ Multiprocessing
        web_server_process = multiprocessing.Process(target=self.server)
        # รัน web_server
        web_server_process.start()

        # Channel Access Token และ URL ของไฟล์สำหรับเก็บรูปภาพใน Line
        ngrok_url = 'https://relaxed-dove-grown.ngrok-free.app'
        image_url = "https://relaxed-dove-grown.ngrok-free.app/MedRecieve.jpg"
        channel_access_token = "o776VQ6aRKQlMK0EbeahQt0AmQAvY8RLv0L5fDGgPqhiccGJZnCa/Efir1W4tdsN03TLojY+CEHcM8sk97XJTc+URIvZLw9IRZvRHPYQmZvnZl65E5Zy2dA5H7m+pkostxNs1Zxlg1Nzwe8CFM3s7wdB04t89/1O/w1cDnyilFU="

        self.send_request_with_header(ngrok_url, 'ngrok-skip-browser-warning', 'true')       # ให้ skip หน้าเว็บ warning
        
        
        try:
            while True:
                
                # Move servo on channel O between extremes.
                now = datetime.now()
                current_time = now.strftime("%H:%M:%S")
                current_day = now.strftime("%A")  # Get the current day of the week
                print(f"ขณะนี้เวลา: {current_time}, วัน: {current_day}")
                
                # hours, minutes, seconds = map(int, current_time.split(':'))
                # time_second = (hours*60*60) + (minutes*60) + seconds
                # print(f"time old:{time_second}")
                
                # beep_process = multiprocessing.Process(target=beep)
                
                if current_time in [before_breakfast, after_breakfast, before_lunch, after_lunch, before_dinner, after_dinner, before_sleep]:
                    
                    row, col, servoNum = self.load_state()
                    while col < self.max_col:
                        while row < self.max_row:  
                            now = datetime.now()
                            current_time = now.strftime("%H:%M:%S")
                            current_day = now.strftime("%A")  # Get the current day of the week
                            print(f"ขณะนี้เวลา: {current_time}, วัน: {current_day}")
                            
                            
                            if current_time in [before_breakfast, after_breakfast, before_lunch, after_lunch, before_dinner, after_dinner, before_sleep]:
                                
                                # pwm.set_pwm(servoNum + 1, 0, servo_min)         #เซอร์โวตัวหลัง
                                # time.sleep(2)
                                
                                # pwm.set_pwm(servoNum, 0, servo_min)             #เซอร์โวตัวหน้า
                                # time.sleep(2)
                                # pwm.set_pwm(servoNum, 0, servo_max)
                                # time.sleep(1)
                                
                                # pwm.set_pwm(servoNum + 1, 0, servo_max)
                                # time.sleep(2)
                                                                    
                                row += 1
                                
                                self.play_recieve_drug_audio()
                                
                                # Line
                                start_time = time.time()            # เก็บเวลาเริ่มต้นเพื่อใช้ในการตรวจสอบระยะเวลา 5 นาที
                                notify_time = 1                     # จำนวนครั้งการแจ้งเตือนไลน์
                                notify_second = 30                  # เวลาในการแจ้งเตือนที่จะเกิดในไลน์
                                max_replay_notify = 3               # จำนวนการแจ้งเตือนไฟล์เสียงที่ไม่ได้รับประทานยา
                                
                                # ไฟล์เสียง beep
                                audio_time = time.time()            # เก็บเวลาเริ่มต้นเพื่อใช้ในการตรวจสอบระยะการเล่นไฟล์เสียง
                                audio_play = 3                      # เล่นไฟล์ใน 3 วินาที
                                
                                # ระยะจากคนและกล่องจ่ายยา (cm)
                                range_user = 15                     # ระยะจากผู้ใช้กับตัวกล่องยา
                                
                                # LED
                                # start_led_time = time.time()
                                # led_play = 3
                                
                                beep_process = multiprocessing.Process(target=self.beep)
                                
                                # # led_blink_process = multiprocessing.Process(target=led_blink)
                                led_blink_process = multiprocessing.Process(target=self.led_blink)
                                led_blink_process.start
                                
                                get_drug = False
                                while True:
                                    
                                    # beep_process.join()
                                    
                                    dist1 = self.distance()
                                    time.sleep(0.2)
                                    dist2 = self.distance()
                                    time.sleep(0.2)
                                    
                                    print ("Measured Distance 1 = %.1f cm" % dist1)
                                    print ("Measured Distance 2 = %.1f cm" % dist2)
                                    self.motion_detect()         # เรียกฟังก์ชันตรวจจับการเคลื่อนไหว
                                    
                                    self.led_blink()
                                    
                                    # if time.time() - start_led_time <= led_play and not get_drug:
                                        
                                    #     start_led_time = time.time()
                                        
                                    
                                    # if not beep_process.is_alive() and time.time() - audio_time >= audio_play and not get_drug:
                                    if time.time() - audio_time >= audio_play and not get_drug:
                                        beep_process = multiprocessing.Process(target=self.beep)
                                        beep_process.start()
                                        # beep_audio()
                                        audio_time = time.time()
                                        
                                    
                                    if dist1 < range_user and dist2 < range_user and GPIO.input(self.GPIO_PIR):          # ตรวจสอบระยะที่ 1 และ 2 เปรียบเทียบเพื่อป้องกันความผิดพลาดของเซนเซอร์ 
                                        get_drug = True                                                          # และใช้ Motion sensor ในการตรวจจับการเคลื่อนไหวที่มารับยา
                                                                        
                                    
                                    # เงื่อนไขการแจ้งเตือนซ้ำ
                                    if time.time() - start_time >= notify_second and notify_time != max_replay_notify:
                                        print(time.time)
                                        print(start_time)
                                        self.wait_receive_line(channel_access_token, notify_time)
                                        notify_time += 1
                                                            
                                        start_time = time.time()
                                    
                                    # เงื่อนไขไม่มารีบยา
                                    if time.time() - start_time >= notify_second and notify_time == max_replay_notify:
                                        self.wait_receive_line(channel_access_token, notify_time)
                                        time.sleep(3)
                                        print("ผู้สูงอายุไม่มารับยา")
                                        # count_audio = 0
                                        notify_time = 1
                                        
                                        # pwm.set_pwm(15, 0, servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                        # time.sleep(2)
                                        # pwm.set_pwm(15, 0, servo_max)
                                        # time.sleep(1)
                                        
                                        self.not_receive_line(channel_access_token)
                                        
                                        break
                                    
                                    # เงื่อนไขถ้ามารับยา
                                    if get_drug:
                                        print("ผู้สูงอายุมารับยาแล้ว")
                                        beep_process.join()
                                        # led_blink_process.join()
                                                                        
                                        capture_image_process = multiprocessing.Process(target=self.capture_image)
                                        capture_image_process.start()
                                        capture_image_process.join()
                                        
                                        self.send_image_to_line(image_url, channel_access_token)
                                        
                                        # time.sleep(60)              # ใช้เมื่อเวลาไม่ใช่ %H:%M:%S แต่เป็น %H:%M
                                        
                                        break
                                    
                                if not row == self.max_row:
                                    self.save_state(row, col, servoNum)  # Save the current state
                                
                                time.sleep(1)
                                
                        # เพิ่มเงื่อนไขที่ถ้า row = 3 ให้กลับไปที่ 0
                        if row == self.max_row:
                            row = 0
                        col += 1
                        servoNum += 2               # จำนวนเซอร์โว 2 ตัว และไปคอลัมน์ถัดไป
                        if not col == self.max_col:
                            self.save_state(row, col, servoNum)  # Save the current state
                        
                    col = 0
                    servoNum = 0
                    self.save_state(row, col, servoNum)  # Save the current state
                    
                                
                time.sleep(1)  # Check the time every second
                
        except KeyboardInterrupt:
            print("\nถูกหยุดการทำงานโดยผู้ใช้")
            GPIO.cleanup()
            
if __name__ == "__main__":
    dispenser = MedicineDispenser()
    dispenser.run()