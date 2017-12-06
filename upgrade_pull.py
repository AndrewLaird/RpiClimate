from urllib.request import urlretrieve
import zipfile
import sys


if __name__ ==  "__main__":
    # determine wheter an upgrade is necessary
    mac = sys.argv[1]
    print(mac)
    build_url = "None"
    build_url = "http://poems.calit2.uci.edu/poems/RPiClimate_update/2017/11/27/RpiClimate.zip"

    # if it is use the url provided to download the zipped file
    if (build_url != "None"):
        # downloading the zipfile
        # build = requests.urlopen(build_url)
        # build_zip = open("/home/andrew/upgrade/build.zip","w")
        urlretrieve(build_url, "/home/andrew/upgrade/build.zip")

        # unzip the file in a folder called upgrade
        zip_ref = zipfile.ZipFile("/home/andrew/upgrade/build.zip", 'r')
        zip_ref.extractall("/home/andrew/upgrade")
        zip_ref.close()
        # then in a shell script outside of RPiClimate, replace the folders and directories with the new upgraded ones
        print("Sucess") #using std out to interface with shell
    print("None")#using std out to interface with shell
