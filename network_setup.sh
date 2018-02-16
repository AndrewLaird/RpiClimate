#currently the network should work without this

#first change wpa_supplicant
sudo bash -c "cat /home/pi/RpiClimate/wpa_supplicant.conf >> /etc/wpa_supplicant/wpa_supplicant.conf"

#then change the interfaces to use that file
sudo bash -c "cat /home/pi/RpiClimate/interfaces >> /etc/network/interfaces"

#then restart the network to get it running
sudo ifconfig wlan1 down
sudo ifconfig wlan1 up

#using wlan1 assume that we are using the antennas and not the onboard wifi which I could not get to connect