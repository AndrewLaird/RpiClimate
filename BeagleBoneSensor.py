#import RPi.GPIO as GPIO
import Adafruit_BBIO.GPIO as GPIO


import time
if __name__ == "__main__":
    GPIO.setup("USR0",GPIO.OUT)
    GPIO.output("USR0",GPIO.HIGH)
    time.sleep(1)
    GPIO.output("USR0",GPIO.LOW)