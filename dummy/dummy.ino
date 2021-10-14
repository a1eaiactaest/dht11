// send dummy data
int id = 3; // station id
float pres = 1000.3;
float gas_res = 124.23; // ohms or kohms
float a_temp = 24.34; // temperature in *C
float a_hum = 61.57; // humidity %
float gd_temp = 15.12; 
float gd_hum = 71.3;

float val_array[] = {id, pres, gas_res, a_temp, a_hum, gd_temp, gd_hum};
int n = sizeof(val_array)/sizeof(float);

void setup(){
  Serial.begin(9600);
}

void loop(){
  delay(2000);
  for (int i=0; i<n; i++){
    Serial.print(val_array[i]);
    Serial.print(" ");
  }
  Serial.println();
}
