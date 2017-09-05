#create a virtual env and put yourself in it
sudo apt-get install python-pip

sudo pip install virtualenv

mkdir ~/.virtualenvs

sudo pip install virtualenvwrapper
export WORKON_HOME=~/.virtualenvs

. /usr/local/bin/virtualenvwrapper.sh
source .bashrc

mkvirtualenv sensor

workon sensor

#sudo easy_install pip #pip installer


sudo apt-get install python-dev  # for python2.x installs

#Adafruit GPIO https://github.com/adafruit/Adafruit_Python_GPIO
sudo apt-get update
sudo apt-get install build-essential python-pip python-dev python-smbus gitdzgasdffadsf
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
pip install Adafruit_GPIO
cd ..


#beaglebone
/usr/bin/ntpdate -b -s -u pool.ntp.org
opkg update && opkg install python-pip python-setuptools
pip install Adafruit_BBIO

#getting the BME Library
git clone https://github.com/adafruit/Adafruit_Python_BME280.git
cd Adafruit_Python_BME280
sudo python setup.py install
cd ..

#installing requests
pip install requests

