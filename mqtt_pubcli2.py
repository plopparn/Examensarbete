#MQTT client demo
#Will continuasly monitor MQTT topics for data check if the recived data matches commands

import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import time
import statistics
import sys

numberOfMessages = 0
totalTime = 0;
allValues = [];

topic = sys.argv[1];
numberOfMessagesCap = int(sys.argv[2]);

def on_connect(client, userdata, flags, rc):
    global topic
    print("Connected with result code "+str(rc)+ " to the topic " +str(topic) + " nr messages: " + str(numberOfMessagesCap))
    client.subscribe(topic)
    
def on_message(client, userdata, msg):
    global numberOfMessages
    global totalTime
    global allValues
    
    allValues.append(int(float(time.time()*1000))-int(float(msg.payload)));
    totalTime += int(float(time.time()*1000))-int(float(msg.payload));
    
    numberOfMessages+=1;
    if numberOfMessages <=1:
        print("running");
    
    if numberOfMessages <= numberOfMessagesCap:
        pub_message()
    else:   
        #out=("Process: "+ str(topic) +"      Total time ended as: " + str(totalTime) +"ms       the avrage time was: " + str(totalTime/numberOfMessages) + "ms when sending "+str(numberOfMessages)+ " messages"+  "       STD: "+ str(statistics.stdev(allValues))+ "ms" )
        #out=(str(totalTime) +" " + str(numberOfMessages) + " "+str(totalTime/numberOfMessages)+ " "+str(statistics.stdev(allValues)))
        #out=(str(totalTime));
        endTimetxt = 'endTime' + str(topic) +'.txt';
        
        with open(endTimetxt, 'w') as f:
            endTime = int(float(time.time()*1000));
            f.write(str(endTime)+" ");
        
        #outputFile = topic+'.txt';
        #with open(outputFile, 'w') as f:
        #    f.write(out);
        
        tempString = "";
        for x in range(len(allValues)-1):
            tempString = tempString + " " + str(allValues[x]);
        
        fileName = str(topic)+'AllValues.txt'
        with open(fileName, 'w') as f:
            f.write(tempString);
        
        print("at sleep");
        time.sleep(3)
        exit(101); 

def pub_message():
    global topic
    startTime = int(float(time.time()*1000));    
    publish.single(topic, str(startTime), hostname="192.168.1.5");
    

#create an MQTT client and attatch our routines to it

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.1.5", 1883, 10)
#client.connect("broker.hivemq.com", 1883, 10)

client.loop_forever()
