import RPi.GPIO as GPIO
import time

servoPIN1 = 17
servoPIN2 = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN1, GPIO.OUT)
GPIO.setup(servoPIN2, GPIO.OUT)

p = GPIO.PWM(servoPIN1, 50) # GPIO 17 for PWM with 50Hz
g = GPIO.PWM(servoPIN2, 50) # GPIO 18 for PWM with 50Hz

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

GPIO.cleanup()
