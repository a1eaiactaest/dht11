// send dummy data
int stations[3] = {3,5,11};
//int id = 3; // station id, random now
float pres = 1000.3;
float gas_res = 124.23; // ohms or kohms
float a_temp = 24.34; // temperature in *C
float a_hum = 61.57; // humidity %
float gd_temp = 15.12; 
float gd_hum = 71.3;

float val_array[] = {pres, gas_res, a_temp, a_hum, gd_temp, gd_hum};
int n = sizeof(val_array)/sizeof(float);

void setup(){
  Serial.begin(9600);
}

void loop(){
  delay(1000);
  int random_index = random(3);
  int id = stations[random_index];
  Serial.print(id);
  Serial.print(" ");
  for (int i=0; i<n; i++){
    Serial.print(val_array[i]);
    Serial.print(" ");
  }
  Serial.println();
}
