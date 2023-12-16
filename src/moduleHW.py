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

# Import the PCA9685 module.
import Adafruit_PCA9685

# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)


#set GPIO Pins Ultrasonic Sensor
GPIO_TRIGGER = 18 
GPIO_ECHO = 24

#set GPIO Pins Motion Sensor
GPIO_PIR = 23
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_PIR, GPIO.IN)

####################### สำหรับ Ultrasonic Sensor ########################

def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
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
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 600  # Max pulse length out of 4096

max_col = 2
max_row = 2

state_file = 'servo_state.txt'

def save_state(row, col, servoNum):
    with open(state_file, 'w') as f:
        f.write(f'{row},{col},{servoNum}')

def load_state():
    if os.path.exists(state_file):
        with open(state_file, 'r') as f:
            content = f.read().split(',')
            state = (int(content[0]), int(content[1]), int(content[2]))
            print(f'Loaded state: {state[0]},{state[1]},{state[2]}')
            return state
    return 0, 0, 0  # default values if the file doesn't exist


# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(60)

########################################################################

############################# สำหรับ Audio ##############################

def play_auido():
    # Initialize Pygame
    pygame.init()
    clock = pygame.time.Clock()

    # Print current time
    the_time = time.strftime("%H:%M:%S", time.localtime())
    print(the_time)

    # Play Sound
    print("เล่นไฟล์เสียง")
    pygame.mixer.init()
    pygame.mixer.music.load("mario.mp3")
    pygame.mixer.music.play()

    # Wait for the sound to finish playing
    while pygame.mixer.music.get_busy():
        clock.tick(1)

    # Clean up Pygame
    pygame.mixer.quit()
    pygame.quit()
    
########################################################################

########################### สำหรับรัน Server #############################

def server():
    subprocess.run(["./server.sh"])
    
########################################################################

############################# สำหรับถ่ายภาพ ##############################

def capture_image():
    subprocess.run(["./capture_image.sh"])
    
########################################################################

########################## สำหรับ PIR Sensor ############################

def motion_detect():
    # print("Waiting for sensor to settle")
    time.sleep(0.2)                   #Waiting 2 seconds for the sensor to initiate
    # print("Detecting motion")

    if GPIO.input(GPIO_PIR):             #Check whether pir is HIGH
        print("Motion Detected!")
        time.sleep(0.2)              #D1- Delay to avoid multiple detection
        time.sleep(0.1)  #While loop delay should be less than detection delay

########################################################################

##################### สำหรับ Line Messaging API #########################

# ส่งรูปภาพเมื่อมารับยา
def send_image_to_line(image_url, channel_access_token):
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
    
def not_receive_line(channel_access_token):
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
    
########################################################################

before_breakfast = "12:38:30"
after_breakfast = "12:55:40"
before_lunch = "12:55:50"
after_lunch = "12:56:00"
before_dinner = "12:56:10"
after_dinner = "12:56:20"
before_sleep = "12:56:30"
    
print('Moving servo on channel 0, press Ctrl-C to quit...')

# รัน Process แบบ Multiprocessing
web_server_process = multiprocessing.Process(target=server)
capture_image_process = multiprocessing.Process(target=capture_image)

# รัน web_server
web_server_process.start()

# Channel Access Token และ URL ของไฟล์สำหรับเก็บรูปภาพใน Line
image_url = "https://relaxed-dove-grown.ngrok-free.app/MedRecieve.jpg"
channel_access_token = "o776VQ6aRKQlMK0EbeahQt0AmQAvY8RLv0L5fDGgPqhiccGJZnCa/Efir1W4tdsN03TLojY+CEHcM8sk97XJTc+URIvZLw9IRZvRHPYQmZvnZl65E5Zy2dA5H7m+pkostxNs1Zxlg1Nzwe8CFM3s7wdB04t89/1O/w1cDnyilFU="

try:
    while True:
        
        # Move servo on channel O between extremes.
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_day = now.strftime("%A")  # Get the current day of the week
        print(f"ขณะนี้เวลา: {current_time}, วัน: {current_day}")
        if current_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] and \
        current_time in [before_breakfast, after_breakfast, before_lunch, after_lunch, before_dinner, after_dinner, before_sleep]:
            
            row, col, servoNum = load_state()
            while col < max_col:
                while row < max_row:  
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
                        
                        play_auido()
                        
                        start_time = time.time()  # เก็บเวลาเริ่มต้นเพื่อใช้ในการตรวจสอบระยะเวลา 5 นาที
                        
                        count_audio = 0
                        while True:
                            get_drug = False
                            notify_time = 30
                            max_replay_notify = 2               # จำนวนการแจ้งเตือนไฟล์เสียง (ไม่นับการแจ้งเตือนครั้งแรกสุด)
                            range_user = 15                     # ระยะจากผู้ใช้กับตัวกล่องยา
                            
                            dist1 = distance()
                            time.sleep(0.2)
                            dist2 = distance()
                            time.sleep(0.2)
                            
                            print ("Measured Distance 1 = %.1f cm" % dist1)
                            print ("Measured Distance 2 = %.1f cm" % dist2)
                            
                            motion_detect()         # เรียกฟังก์ชันตรวจจับการเคลื่อนไหว
                            
                            if dist1 < range_user and dist2 < range_user and GPIO.input(GPIO_PIR):          # ตรวจสอบระยะที่ 1 และ 2 เปรียบเทียบเพื่อป้องกันความผิดพลาดของเซนเซอร์ 
                                get_drug = True                                                             # และใช้ Motion sensor ในการตรวจจับการเคลื่อนไหวที่มารับยา
                                     
                            
                            # เงื่อนไขการแจ้งเตือนซ้ำ
                            if time.time() - start_time >= notify_time and count_audio != max_replay_notify:
                                play_auido()
                                count_audio += 1
                                # print(count_audio)
                                start_time = time.time()
                            
                            # เงื่อนไขไม่มารีบยา
                            if time.time() - start_time >= notify_time and count_audio == max_replay_notify:
                                print("ผู้สูงอายุไม่มารับยา")
                                count_audio = 0
                                
                                # pwm.set_pwm(15, 0, servo_min)             # เซอร์โวมอเตอร์สำหรับช่องทิ้งยา
                                # time.sleep(2)
                                # pwm.set_pwm(15, 0, servo_max)
                                # time.sleep(1)
                                
                                not_receive_line(channel_access_token)
                                
                                break
                            
                            # เงื่อนไขถ้ามารับยา
                            if get_drug:
                                print("ผู้สูงอายุมารับยาแล้ว")
                                
                                capture_image_process.start()
                                
                                send_image_to_line(image_url, channel_access_token)
                                
                                count_audio = 0
                                break
                        
                        if not row == max_row:
                            save_state(row, col, servoNum)  # Save the current state
                        
                    else:
                        time.sleep(1)
                        
                # เพิ่มเงื่อนไขที่ถ้า row = 3 ให้กลับไปที่ 0
                if row == max_row:
                    row = 0
                col += 1
                servoNum += 2               # จำนวนเซอร์โว 2 ตัว และไปคอลัมน์ถัดไป
                if not col == max_col:
                    save_state(row, col, servoNum)  # Save the current state
                
            col = 0
            servoNum = 0
            save_state(row, col, servoNum)  # Save the current state
            
                        
        time.sleep(1)  # Check the time every second
        
except KeyboardInterrupt:
    print("\nถูกหยุดการทำงานโดยผู้ใช้")
    GPIO.cleanup()