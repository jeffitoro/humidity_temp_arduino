#include <dht.h>
#define DHT11_PIN 8
#define LEDPIN_H 13
#define LEDPIN_T 12

dht DHT;
char receivedChar;
boolean newData = false;
/*
int ledPinH = 13;
int ledPinT = 12;
*/
/*

void loop()
{
  int chk = DHT.read11(DHT11_PIN);
  Serial.println("{\"temperature\":" + String(DHT.temperature)+ ", \"humidity\" :" + String(DHT.humidity) + "}");
  delay(2000);
}
*/
void setup()
{
  pinMode(LEDPIN_H, OUTPUT);
  pinMode(LEDPIN_T, OUTPUT);
  /*analogWrite(LEDPIN_H, 255);
  analogWrite(LEDPIN_T, 255);*/
  Serial.begin(9600);
} 

void loop()
{
  
  DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  
  if(DHT.humidity > 50){
    Serial.println("c'est trop humide");
    //digitalWrite(ledPinH, HIGH);
    analogWrite(LEDPIN_H, 255);
    delay(2000);
    digitalWrite(LEDPIN_H, LOW);
    analogWrite(LEDPIN_H, 0);
  }else{
    Serial.println("c'est une humidité normal");
    digitalWrite(LEDPIN_H, LOW);
  }
  if(DHT.temperature > 22){
    Serial.println("c'est trop humide");
    digitalWrite(LEDPIN_T, HIGH);
  }else{
    Serial.println("c'est une humidité normal");
    digitalWrite(LEDPIN_T, LOW);
  }
  delay(2000);
} 
void recvInfo() {

  if (Serial.available() > 0) {

    receivedChar = Serial.read();
    newData = true;
    
  }
  
}
void lightLED() {

  int led = (receivedChar - '0');

  while(newData == true) {

    digitalWrite(led, HIGH);
    delay(2000);
    digitalWrite(led, LOW);

    newData = false;
    
  }
  
}
