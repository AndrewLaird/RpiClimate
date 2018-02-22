#this file takes the directory in side of ~/upgrade and replaces everything in RPiClimate with its new copy
MAC="$(ifconfig -a |grep -Po "(?:ether|HWaddr) \K[^\s]*" | head -1)"
echo $MAC
RESULT="$(python3 ~/RpiClimate/upgrade_pull.py $MAC)"
echo "result"
echo $RESULT

if [ "$RESULT" = "Sucess" ]; then
    sudo cp -R /home/pi/upgrade/RpiClimate /home/pi/
    echo "upgrade complete"
else
    echo "up to date"
fi