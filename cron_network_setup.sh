sudo cp /home/pi/ZigbeeReplacement/network_configuration /etc/wpa_supplicant/wpa_supplicant.conf

#restart the network
sudo ifdown wlan0
sudo ifup wlan0


#add to the crontab
echo ""*/15 * * * * root python /home/pi/ZigbeeReplacement/SensorPutRequest.py" >> /etc/crontab.d/sensor_put_crontab
