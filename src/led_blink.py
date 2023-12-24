import RPi.GPIO as GPIO
import time

# Set the GPIO mode to BCM
GPIO.setmode(GPIO.BCM)

# Set up GPIO pin 16 as an output
led_pin = 16
GPIO.setup(led_pin, GPIO.OUT)

try:
    while True:
        # Turn the LED on
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(1)  # Pause for 1 second

        # Turn the LED off
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(1)  # Pause for 1 second

except KeyboardInterrupt:
    # If a keyboard interrupt (Ctrl+C) is detected, clean up GPIO
    GPIO.cleanup()
