mkdir lib
cd lib
#Adafruit GPIO https://github.com/adafruit/Adafruit_Python_GPIO
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus gitdzgasdffadsf
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install


#beaglebone
/usr/bin/ntpdate -b -s -u pool.ntp.org
opkg update && opkg install python-pip python-setuptools
pip install Adafruit_BBIO

#getting the BME Library
git clone https://github.com/adafruit/Adafruit_Python_BME280.git
cd Adafruit_Python_BME280
sudo python setup.py install

#going back up
cd ../..

