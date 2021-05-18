#MQTT pulbisher

import paho.mqtt.publish as publish
import time
import sys
#message = raw_input("Please enter your message: ")
#topic = raw_input("Please enter what topic you want to post this on: ")

#message = "message";
#topic = "testTopic";

#message = "message";
#topic = "testTopic";

#print("published message: "+message+ " to the topic: " + topic)
#print("Pulishfunction has been executed")
#for x in range(1000):
r = int(sys.argv[1])
for x in range(r):
    topic = "time"+str(x)
    message = str(time.time()*1000);
    publish.single(topic, message, hostname="192.168.1.5");

#print("Pulishfunction has been executed")

