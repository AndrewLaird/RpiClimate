#import RPi.GPIO as GPIO
#import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BME280 import *
import requests



def getMAC(interface='wlan0'):
  # Return the MAC address of the specified interface
  try:
    str = open('/sys/class/net/%s/address' %interface).read()
  except:
    str = "00:00:00:00:00:00"
  return str[0:17]

def main():

    sensor = BME280(t_mode=BME280_OSAMPLE_8, p_mode=BME280_OSAMPLE_8, h_mode=BME280_OSAMPLE_8)

    degrees = sensor.read_temperature()
    pascals = sensor.read_pressure()
    hectopascals = pascals / 100
    humidity = sensor.read_humidity()

    mac = getMAC(interface='wlan0')

    data = '{"temperature":'+str(degrees)+',"pressure":'+str(pascals)+',"humidity":'+str(humidity)+',"MAC":'+str(mac)+'}'
    print(data)
    response = requests.put("http://poems.calit2.uci.edu/poems/sensor_input",data=data)
    print(response)
    return (response)
import time
if __name__ == "__main__":
    main()