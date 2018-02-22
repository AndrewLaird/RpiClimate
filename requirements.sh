#get pip
sudo apt-get -y install python-pip

sudo apt-get -y install python-dev  # for python2.x installs

#Adafruit GPIO https://github.com/adafruit/Adafruit_Python_GPIO
sudo apt-get -y update
sudo apt-get -y install build-essential python-pip python-dev python-smbus gitdzgasdffadsf
sudo git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
cd Adafruit_Python_GPIO
sudo python setup.py install
pip install Adafruit_GPIO
cd ..

#getting the BME Library
sudo git clone https://github.com/adafruit/Adafruit_Python_BME280.git
cd Adafruit_Python_BME280
sudo python setup.py install
#copy all the files out of the folder
sudo cp * ..
#exit directory
cd ..



#getting pipenv for requests
pip install pipenv

#installing requests
pipenv install requests

#setup cron
. cron_setup.sh

#making sure there is a directory for upgrading
mkdir /home/pi/upgrade

echo "You Must enable I2C"
echo "run sudo raspi-config"
echo "Also setup ssh in the same way"
