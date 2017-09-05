import smtplib
from json import load
from urllib2 import urlopen

my_ip = load(urlopen('http://jsonip.com'))['ip']

SERVER = "localhost"

FROM = "alaird@gmail.com"
TO = ["alaird@gmail.com"] # must be a list

SUBJECT = "Hello!"

TEXT = "Hey the new ip is " + str(my_ip)

# Prepare actual message

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP(SERVER)
server.sendmail(FROM, TO, message)
server.quit()