// rf95_client.pde
// -*- mode: C++ -*-
// Example sketch showing how to create a simple messageing client
// with the RH_RF95 class. RH_RF95 class does not provide for addressing or
// reliability, so you should only use RH_RF95 if you do not need the higher
// level messaging abilities.
// It is designed to work with the other example rf95_server
// Tested with Anarduino MiniWirelessLoRa, Rocket Scream Mini Ultra Pro with
// the RFM95W, Adafruit Feather M0 with RFM95

#include <RH_RF95.h>
#include <Wire.h>
#include <SPI.h>
#include <Adafruit_Sensor.h>
#include "Adafruit_BME680.h"
#include <OneWire.h> 
#include <DallasTemperature.h>

// Singleton instance of the radio driver
//RH_RF95 rf95;
//RH_RF95 rf95(5, 2); // Rocket Scream Mini Ultra Pro with the RFM95W
RH_RF95 rf95(8, 3); // Adafruit Feather M0 with RFM95 

// Need this on Arduino Zero with SerialUSB port (eg RocketScream Mini Ultra Pro)
//#define Serial SerialUSB

//---BME---
#define BME_SCK A0
#define BME_MISO A1
#define BME_MOSI A2
#define BME_CS A3

#define SEALEVELPRESSURE_HPA (1013.25)

//Adafruit_BME680 bme; // I2C
//Adafruit_BME680 bme(BME_CS); // hardware SPI
Adafruit_BME680 bme(BME_CS, BME_MOSI, BME_MISO,  BME_SCK);

//---Soil Temp---
#define ONE_WIRE_BUS A5

OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature sensors(&oneWire);

//---Vars---

int ar[40];
int l = 0;

//---Func---

int leng(int x){
  int i = 1;
  x /= 10;
  while(x != 0){
    x /= 10;
    i++;
  }
  return i;
}

int wh(int y){
  int x;
  switch(y){
    case 1:
      x = bme.pressure;
      Serial.print("Pressure = ");
      Serial.print(x / 100.0);
      Serial.println(" hPa");
      break;
    case 2:
      x = bme.gas_resistance;
      Serial.print("Gas = ");
      Serial.print(x / 1000.0);
      Serial.println(" KOhms");
      break;
    case 3:
      x = bme.temperature*1000L;
      Serial.print("Temperature = ");
      Serial.print(x / 1000.0);
      Serial.println(" *C");
      break;
    case 4:
      x = bme.humidity*1000L;
      Serial.print("Humidity = ");
      Serial.print(x / 1000.0);
      Serial.println(" %");
      break;
    case 5:
      sensors.requestTemperatures();
      x = sensors.getTempCByIndex(0)*1000L;
      Serial.print("Ground Temp = ");
      Serial.print(x / 1000.0); 
      Serial.println(" *C");
      break;
    case 6: {
      float a = analogRead(A4);
      x = a / 9.5 * 1000L;
      Serial.print("Ground Hum = ");
      Serial.print(x / 1000.0); 
      Serial.println(" %");
      break; }
    case 7:
      x = 11;
      Serial.print("id: "); 
      Serial.println(x);
      break; 
      
  }
  return x;
}

char det(int x){
  if (x >= 0) return 'p';
  else if (x < 0) return 'n';
}

int en(){
  int j = 0;
  int a, b, c, d, ll;
  int le = 0;
  for(int i = 1; i < 8; i++){
    a = wh(i);
    d = a;
    if (a < 0) a *= -1;
    ll = leng(a);
    le += ll;
    for(int ii = 0; ii < ll; ii++){
      b = pow(10, ll-ii-1);
      c = a / b;
      ar[j] = c;
      c = c*b;
      a -= c;
      j++;
    }
    ar[j] = det(d);
    j++;
  }
  ar[j-1] = 'e';
  return le;
}

void setup() 
{
  // Rocket Scream Mini Ultra Pro with the RFM95W only:
  // Ensure serial flash is not interfering with radio communication on SPI bus
//  pinMode(4, OUTPUT);
//  digitalWrite(4, HIGH);

  Serial.begin(9600);
  //  while (!Serial) ; // Wait for serial port to be available
  if (!rf95.init())
    Serial.println("init failed");
  Serial.println(F("BME680 test"));
  //----BME----
  if (!bme.begin()) {
    Serial.println("Could not find a valid BME680 sensor, check wiring!");
    while (1);
  }
  
  // Set up oversampling and filter initialization
  bme.setTemperatureOversampling(BME680_OS_8X);
  bme.setHumidityOversampling(BME680_OS_2X);
  bme.setPressureOversampling(BME680_OS_4X);
  bme.setIIRFilterSize(BME680_FILTER_SIZE_3);
  bme.setGasHeater(320, 150); // 320*C for 150 ms
  
  //----Soil Temp---
  sensors.begin(); 
}

void loop()
{
  if (! bme.performReading()) {
    Serial.println("Failed to perform reading :(");
    return;
  }
  Serial.println("Sending to rf95_server");
  // Send a message to rf95_server

  l = en();
  l += 7;
  
  uint8_t m[l];
  for(int i = 0; i < l; i++){
    m[i] = ar[i];
  }
  
  rf95.send(m, sizeof(m));
  
  rf95.waitPacketSent();
  // Now wait for a reply
  uint8_t buf[RH_RF95_MAX_MESSAGE_LEN];
  uint8_t len = sizeof(buf);

  if (rf95.waitAvailableTimeout(3000))
  { 
    // Should be a reply message for us now   
    if (rf95.recv(buf, &len))
   {
      Serial.print("got reply: ");
      Serial.println((char*)buf);
    //      Serial.print("RSSI: ");
    //      Serial.println(rf95.lastRssi(), DEC);    
    }
    else
    {
      Serial.println("recv failed");
    }
  }
  else
  {
    Serial.println("No reply, is rf95_server running?");
  }
  delay(2000);
}
