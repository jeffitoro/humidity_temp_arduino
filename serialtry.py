# encoding:utf-8
import serial
import requests
import json
import RPi.GPIO as GPIO
import time

serialport = serial.Serial("/dev/ttyACM0",9600,timeout=0.5)
url ='https://api.thingspeak.com/apps/thinghttp/send_request?api_key=VQX7ZL0145XOB43J'
urlGet = 'https://api.thingspeak.com/talkbacks/24302/commands/execute.json?api_key=GVDMQ1NQ229NDJBV'
headers = {'Content-type': 'application/json'}
Led1 = 'H'
Led2 = 'T'
hMax = 50
hMin = 10
tMax = 30
tMin = 18
namePlant = " l'une de vos plante "
while True:
    getInfo = requests.post(urlGet)
    getInfojson = getInfo.json()
    command = serialport.readline()
    a = command.decode('utf-8')
    print(a[:-2])
    if len(a[:-2])>38:
        print(getInfojson)
        jsonresult = json.loads(a[:-2])
        if "command_string" in getInfojson:
            jsonobjet = json.loads(str(getInfojson["command_string"]))
            if jsonobjet:
                hMax = float(jsonobjet["humMax"])
                hMin = float(jsonobjet["humMin"])
                tMax = float(jsonobjet["tempMax"])
                tMin = float(jsonobjet["tempMin"])
                if "Name" in jsonobjet and jsonobjet["Name"]:
                    namePlant = jsonobjet["Name"]
        if "humidity" in jsonresult and (float (jsonresult["humidity"]) > hMax or float (jsonresult["humidity"]) < hMin) :
            serialport.flush()
            temp1 = str(Led1)
            serialport.write(b'H')
            msg = "L'humidité de "+ str(namePlant) +" n'est pas comprise entre "+str(hMin)+" et "+str(hMax)+", la valeur actuelle est: "+str(int(jsonresult["humidity"]))
            data = {
                'message': msg
            }
            print(msg)
            response = requests.post(url, data=json.dumps(data), headers=headers)
            
        if "temperature" in jsonresult and (float (jsonresult["temperature"]) > tMax or float (jsonresult["temperature"]) < tMin):
            serialport.flush()
            temp2 = str(Led2)
            serialport.write(b'T')
            print("LED on 13")
            time.sleep(2)
            msg = "La temperature de "+ str(namePlant) +" n'est pas comprise entre "+str(tMin)+" et "+ str(tMax)+", la valeur actuelle est: "+str(int(jsonresult["temperature"]))
            data = {
                'message': msg
            }
            print(msg)
            response = requests.post(url, data=json.dumps(data), headers=headers)
