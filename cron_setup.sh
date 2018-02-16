#add to the crontab
#this should only be run on intial startup
sudo bash -c "echo \"*/15 * * * * root /usr/bin/python /home/pi/RpiClimate/SensorPutRequest.py\" >> /etc/crontab"