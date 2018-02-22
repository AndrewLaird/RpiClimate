from urllib.request import urlretrieve
import urllib.request, urllib.parse
import zipfile
import sys


if __name__ ==  "__main__":
    # determine wheter an upgrade is necessary
    mac = sys.argv[1]
    data = {
        'mac': mac,
    }
    data = bytes(urllib.parse.urlencode(data).encode())
    handler = urllib.request.urlopen('http://poems.calit2.uci.edu/poems/RPiClimate_CheckIn', data);
    status = handler.getcode()
    build_url = handler.read().decode( 'utf-8' )
    # if it is use the url provided to download the zipped file
    if (status == 200):
        # downloading the zipfile
        urlretrieve(build_url, "/home/pi/upgrade/build.zip")

        # unzip the file in a folder called upgrade
        zip_ref = zipfile.ZipFile("/home/pi/upgrade/build.zip", 'r')
        zip_ref.extractall("/home/pi/upgrade")
        zip_ref.close()
        # then in a shell script outside of RPiClimate, replace the folders and directories with the new upgraded ones
        print("Sucess") #using std out to interface with shell
    else:
        print("None")#using std out to interface with shell
