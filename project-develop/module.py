import RPi.GPIO as GPIO
import time
from datetime import datetime
import pygame
import sqlite3

servoPIN1 = 17
servoPIN2 = 18
GPIO_TRIGGER = 23 
GPIO_ECHO = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

p = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
g = GPIO.PWM(servoPIN2, 50) # GPIO 18 for PWM with 50Hz+

#conn = sqlite3.connect('medicine.db')
#cursor = conn.cursor()
#conn.commit()

pygame.init()
clock = pygame.time.Clock()

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

try:
    while True:
        
        clock.tick(1)
        
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(f"Current Time: {current_time}")
        
        dist = distance()
        print ("Measured Distance = %.1f cm\n" % dist)
        time.sleep(1)
        
        set_time = "13:33:00"
        #cursor.execute("SELECT time FROM Meal WHERE time=?", (,))
        #result = cursor.fetchone()
        
        ###################### กลไกทำงาน #################################
        #if current_time == result:
        if current_time == set_time:   
            ################## Servo ####################
            p.start(3) # Initialization
            g.start(12.5) # Initialization
            
            time.sleep(3)
            g.ChangeDutyCycle(3)
            time.sleep(3)
            p.ChangeDutyCycle(12.5)
            time.sleep(3)
            p.ChangeDutyCycle(3)
            time.sleep(5)
            g.ChangeDutyCycle(12.5)
            time.sleep(1)
            
            p.stop()
            g.stop()
            
            ################## เล่นไฟล์เสียง ####################
            time.sleep(1)
            print("Play Sound!!")
            pygame.mixer.init()
            pygame.mixer.music.load("sound.mp3")
            pygame.mixer.music.play()
            
            start_time = time.time()  # เก็บเวลาเริ่มต้นเพื่อใช้ในการตรวจสอบระยะเวลา 5 นาที
            
            while True:
                get_drug = False
                
                dist1 = distance()
                time.sleep(0.2)
                dist2 = distance()
                time.sleep(0.2)
                
                if dist1 < 15 and dist2 < 15:
                    get_drug = True
                
                # เงื่อนไขไม่มารีบยา
                if time.time() - start_time >= 30:
                    print("ผู้สูงอายุไม่มารับยา")
                    break
                
                # เงื่อนไขถ้ามารับยา
                if get_drug:
                    print("ผู้สูงอายุมารับยาแล้ว")
                    break
            
            ##### Sound ####
            
            #time.sleep(60)
            #print("Play Sound!!")
            #pygame.mixer.init()
            #pygame.mixer.music.load("sound.mp3")
            #pygame.mixer.music.play()
            
except KeyboardInterrupt:
    p.stop()
    g.stop()
    pygame.mixer.music.stop()  # หยุดการเล่นเสียง

    GPIO.cleanup()


