  // rf95_server.pde
// -*- mode: C++ -*-
// Example sketch showing how to create a simple messageing server
// with the RH_RF95 class. RH_RF95 class does not provide for addressing or
// reliability, so you should only use RH_RF95  if you do not need the higher
// level messaging abilities.
// It is designed to work with the other example rf95_client
// Tested with Anarduino MiniWirelessLoRa, Rocket Scream Mini Ultra Pro with
// the RFM95W, Adafruit Feather M0 with RFM95

#include <SPI.h>
#include <RH_RF95.h>

// Singleton instance of the radio driver
//RH_RF95 rf95;
//RH_RF95 rf95(5, 2); // Rocket Scream Mini Ultra Pro with the RFM95W
RH_RF95 rf95(8, 3); // Adafruit Feather M0 with RFM95 

// Need this on Arduino Zero with SerialUSB port (eg RocketScream Mini Ultra Pro)
//#define Serial SerialUSB

int led = 9; 

float p, voc, ta, ha, tg, hg;
int id;

void wh(int x, int y){
  switch(y){
    case 1:
      p = x;
      break;
    case 2:
      voc = x;
      break;
    case 3:
      ta = x / 1000.0;
      break;
    case 4:
      ha = x / 1000.0;
      break;
    case 5:
      tg = x / 1000.0;
      break;
    case 6:
      hg = x / 1000.0;
      break;
    case 7:
      id = x;
      break;
  }
}

void de(int x[]){
  int i = 0;
  int a = x[i];
  int b = 0;
  int j = 0;
  while (a != 'e'){
    a = x[i];
    while (a < 10){
      b = b*10+a;
      i++;
      a = x[i];
    } 
    if(a == 'n') b = b*-1;
    j++;
    wh(b, j);
    b = 0;
    i++;
  } 
}

void setup() 
{
  pinMode(led, OUTPUT);     
  Serial.begin(9600);
  if (!rf95.init())
    Serial.println("init failed");  
}

void loop()
{
  Serial.println("tu dziala");
  Serial.println(rf95.available());
  if (rf95.available())
  {
    Serial.println("tu nie");
    // Should be a message for us now   
    uint8_t m[RH_RF95_MAX_MESSAGE_LEN];
    uint8_t len = sizeof(m);
    if (rf95.recv(m, &len))
    {
      digitalWrite(led, HIGH);
      int ar[len];
      for (int i = 0; i < len; i++){
        ar[i] = m[i];
      }
      de(ar);
      

      char buf[40];
      sprintf(buf, "%d %f %f %f %f %f %f", id, p, voc, ta, ha, tg, hg);
      Serial.println(buf);
      
      // Send a reply
      uint8_t d[] = "OK";
      rf95.send(d, sizeof(d));
      rf95.waitPacketSent();
      digitalWrite(led, LOW);
    }
    else
    {
      Serial.println("recv failed");
    }
  }
  delay(1);
}
