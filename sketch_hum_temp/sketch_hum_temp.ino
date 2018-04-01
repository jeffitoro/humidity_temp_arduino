#include <dht.h>

dht DHT;

#define DHT11_PIN 7

void setup(){
  Serial.begin(9600);
}

void loop()
{
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  if(DHT.humidity > 50){
    Serial.println("c'est trop humide");
  }else{
    Serial.println("c'est une humidité normal");
  }
  delay(2000);
}
