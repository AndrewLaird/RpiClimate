__author__ = 'Cody Giles'
__license__ = "Creative Commons Attribution-ShareAlike 3.0 Unported License"
__version__ = "1.0"
__maintainer__ = "Cody Giles"
__status__ = "Production"

import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import re

import base64

def connect_type(word_list):
    """ This function takes a list of words, then, depeding which key word, returns the corresponding
    internet connection type as a string. ie) 'ethernet'.
    """
    if 'wlan0' in word_list or 'wlan1' in word_list:
        con_type = 'wifi'
    elif 'eth0' in word_list:
        con_type = 'ethernet'
    else:
        con_type = 'current'

    return con_type

# Change to your own account information
# Account Information
to = 'INRFPI@gmail.com' # Email to send to.
gmail_user = 'INRFPI@gmail.com' # Email to send from. (MUST BE GMAIL)
gmail_password = base64.b64decode('UGlJTlJGMjAxNw==').decode("ASCII") # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.


smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server
today = datetime.date.today()  # Get current time/date

arg='ifconfig'  # Linux command to retrieve ip addresses.
# Runs 'arg' in a 'hidden terminal'.
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()  # Get data from 'p terminal'.

#turn the command from byte data to string
output = data[0].decode("ASCII")

#search the output for the ip
regex_pattern = r"inet (?:addr)?[:]?([\d]+.[\d]+.[\d]+.[\d]+)"
ip_posibilities = re.findall(regex_pattern,output)#[^\a-Z]*
print(ip_posibilities)

#get the mac as well
mac_regex_pattern = r"(?:ether|HWaddr) ((?:[^:\s]{2}:){5}[^:\s]{2})"
mac_posibilities = re.findall(mac_regex_pattern,output)
mac = mac_posibilities[0]

#form the message
my_ip_a = "Mac: " + mac + "\n"
my_ip_a = my_ip_a + "possible ip's are:\n"+ "\n".join(ip_posibilities)
# Creates the text, subject, 'from', and 'to' of the message.
msg = MIMEText(my_ip_a )#+ "\n" + my_ip_b)
msg['Subject'] = 'IPs For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
# Sends the message
smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server.
smtpserver.quit()