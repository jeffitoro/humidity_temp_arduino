# encoding:utf-8
import serial
import requests
import json
import RPi.GPIO as GPIO
import time

serialport = serial.Serial("/dev/ttyACM0",9600,timeout=0.5)
url ='https://api.thingspeak.com/apps/thinghttp/send_request?api_key=VQX7ZL0145XOB43J'
headers = {'Content-type': 'application/json'}

while True:
    command = serialport.readline()
    a = command.decode('utf-8')
    
    if a:        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        jsonresult = json.loads(a[:-2])
        print(jsonresult)
        if float (jsonresult["humidity"]) > 50:
            GPIO.setup(12,GPIO.OUT)
            GPIO.output(12,GPIO.HIGH)
            print("LED on 12")
            time.sleep(2)
            msg = "humidité trop haute "+str(int(jsonresult["humidity"]))
            data = {
                'message': msg
            }
            print(msg)
            response = requests.post(url, data=json.dumps(data), headers=headers)
        else:
            GPIO.setup(12,GPIO.OUT)
            GPIO.output(12,GPIO.LOW)
            
        if float (jsonresult["temperature"]) > 18:
            GPIO.setup(13,GPIO.OUT)
            GPIO.output(13,GPIO.HIGH)
            print("LED on 13")
            time.sleep(2)
            msg = "temperature trop haute "+str(int(jsonresult["temperature"]))
            data = {
                'message': msg
            }
            print(msg)
            response = requests.post(url, data=json.dumps(data), headers=headers)
        else:
            GPIO.setup(13,GPIO.OUT)
            GPIO.output(13,GPIO.LOW)
