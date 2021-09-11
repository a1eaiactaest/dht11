#include "DHT.h"
#define DHTPIN 2
#define DHTTYPE DHT11


DHT dht(DHTPIN, DHTTYPE);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  dht.begin();
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(2000);
  float h  = dht.readHumidity();
  float t = dht.readTemperature();
  //float f = dht.readTemperature(true); < for fahrenheit

  if (isnan(h) || isnan(t)){
    Serial.println(F("failed to read from DHT11"));
    return;
  }
  
  // heat index
  float hic = dht.computeHeatIndex(t,h,false);

  Serial.print(h);
  Serial.print(F(" "));
  Serial.print(t);
  Serial.print(F(" "));
  Serial.print(hic);
  Serial.println();
}
