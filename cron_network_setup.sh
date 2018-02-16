sudo cp /home/pi/RpiClimate/network_configuration /etc/wpa_supplicant/wpa_supplicant.conf

#restart the network
sudo ifdown wlan1
sudo ifup wlan1


#add to the crontab
echo ""*/15 * * * * root /bin/python /home/pi/RpiClimate/SensorPutRequest.py" >> /etc/crontab.d/sensor_put_crontab