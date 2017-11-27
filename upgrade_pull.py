import urllib.request
import zipfile

#determine wheter an upgrade is necessary

#if it is use the url provided to download the zipped file
if(False):
    zip_ref = zipfile.ZipFile("necessary path", 'r')
    zip_ref.extractall("~/home/upgrade")
    zip_ref.close()

#unzip the file in a folder called upgrade

#then in a shell script outside of RPiClimate, replace the folders and directories with the new upgraded ones