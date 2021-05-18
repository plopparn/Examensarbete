import subprocess
import sys
import os
import time
import statistics
#subprocess.call("python mqtt_pubcli.py", shell=True)

#print ("arguments: " +str(sys.argv[1]));
inp = 'lxterminal -e  python mqtt_pubcli2.py time'
r = int(sys.argv[1]);
numberOfMessages = int(sys.argv[2]);

for x in range(r):
    newInp =inp+str(x)+' '+str(numberOfMessages);
    subprocess.call([newInp], cwd='/home/pi/Documents', shell=True)

#sleep to await all the clients to start up before transmitting.
time.sleep(20);

argv = 'lxterminal -e  python mqtt_publisher.py '
newArgv = argv+str(r);
subprocess.call([newArgv], cwd='/home/pi/Documents', shell=True)

#to check the total time spent untill compleate.
startingTime = int(float(time.time()*1000));    

#sleep timer to await the other running terminals
#subprocess.call(['vcgencmd measure_temp'], shell=True)

time.sleep(5);

subprocess = subprocess.Popen("vcgencmd measure_volts", shell=True, stdout=subprocess.PIPE)
subprocess_return = subprocess.stdout.read()
print(subprocess_return)

print("sleep begin")
time.sleep(110);
print("sleep over")

#____________________________________________________________________________________________________________________________________

with open('FullAllValues.txt', 'w') as f:
    for x in range(r):
        inputFile = 'time'+str(x)+'AllValues.txt';
        with open(inputFile, 'r') as q:
            f.write(q.read());

AllValuesStringArray = [];            
with open ('FullAllValues.txt', 'r') as f:
    AllValuesStringArray = f.read().split();

AllValuesFloatArray = [];
for x in AllValuesStringArray:
    AllValuesFloatArray.append(float(x))
#____________________________________________________________________________________________________________________________________
#calculating time spend to send x amount of messages:
with open('endTimeCombined.txt', 'w') as f:
    for x in range(r):
        inputFile = 'endTimetime'+str(x)+'.txt';
        with open(inputFile, 'r') as q:
            f.write(q.read());

endTimeStringArray = [];            
with open ('endTimeCombined.txt', 'r') as f:
    endTimeStringArray = f.read().split();

endTimeFloatArray = [];
for x in endTimeStringArray:
    endTimeFloatArray.append(float(x))
TimeForTest = max(endTimeFloatArray)-startingTime;
print (str(TimeForTest));

for x in range(r):
    os.remove('endTimetime'+str(x)+'.txt')
#____________________________________________________________________________________________________________________________________

if (r>1):
    compressedAnalasis = "Time for test: "+ str(TimeForTest) + "ms   Total time: " + str(sum(AllValuesFloatArray)) + "Meanvalue: " + str(statistics.mean(AllValuesFloatArray)) + "ms     Standardavvikelse:" + str(statistics.stdev(AllValuesFloatArray)) + "ms     Antal enheter: " + str(r) + "     Antal meddelanden per enhet: " +str(len(AllValuesFloatArray)/r)+ "   totalt antal meddelanden:" + str(len(AllValuesFloatArray)) +"\n";
    with open ('ComprimeradAnalys.txt', 'a') as f:
        f.write(compressedAnalasis);
else:
    compressedAnalasis = "Time for test: "+ str(TimeForTest) + "ms   Total time: " + str(sum(AllValuesFloatArray)) + "Meanvalue: " + str(statistics.mean(AllValuesFloatArray)) + "ms     Standardavvikelse:" + str(statistics.stdev(AllValuesFloatArray)) + "ms     Antal enheter: " + str(r) + "     Antal meddelanden per enhet: " +str(len(AllValuesFloatArray)/r)+ "   totalt antal meddelanden:" + str(len(AllValuesFloatArray)) +"\n";
    #compressedAnalasis = "Total time: " + str(sum(AllValuesFloatArray)) +"Meanvalue: " + str(statistics.mean(AllValuesFloatArray)) + "      Antal enheter: " + str(r) + "     Antal meddelanden per enhet: " +str(len(AllValuesFloatArray)/r)+ "\n";
    with open ('ComprimeradAnalys.txt', 'a') as f:
        f.write(compressedAnalasis);


#____________________________________________________________________________________________________________________________________
for x in range(r):
    file = "time"+str(x)+"AllValues.txt";
    os.remove(file);

#____________________________________________________________________________________________________________________________________

