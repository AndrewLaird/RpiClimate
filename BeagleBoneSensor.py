#import RPi.GPIO as GPIO
#import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BME280 import *
import requests


import time
if __name__ == "__main__":

    sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()

    data = {"temperature":degrees,"pressure":pascals,"humidity":humidity}

    response = requests.post("http://poems.calit2.uci.edu/poems/Zigbee")

