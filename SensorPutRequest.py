#import RPi.GPIO as GPIO
#import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BME280 import *
import requests
import json
import hashlib


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

    mac = getMAC(interface='eth0')
    salt = "$2b$12$.ghDXmVfgSz9Z8u1nBaBf."
    pi_hash = hashlib.sha256()
    pi_hash.update(bytes(mac))
    pi_hash.update(bytes(salt))
    pi_hash_code = pi_hash.hexdigest()

    data = {"temperature":degrees,"pressure":pascals,"humidity":humidity,"MAC":mac,"code":str(pi_hash_code)}
    data = json.dumps(data)
    print(data)
    response = requests.put("https://poems.calit2.uci.edu/poems/sensor_input",data=data)
    response.close()
    return (response)


if __name__ == "__main__":
    main()
