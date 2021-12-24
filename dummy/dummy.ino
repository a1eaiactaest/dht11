// send dummy data
int stations[3] = {3,5,11};

// send error message once in while ~every 10th line
String error_msg = "Error: Unexpected value inside of message. Data has been dropped.";

void setup(){
  Serial.begin(9600);
}

void loop(){
  delay(1000);

  int random_index = random(3);
  int id = stations[random_index];

  float pres = random(900, 1100);
  float gas_res = random(0, 255);
  float a_temp = random(15, 25);
  float a_hum = random(40, 60);
  float gd_temp = random(0, 10);
  float gd_hum = random(60, 100);


  int is_error = random (0, 10);

  if (is_error == 5){
    Serial.println(error_msg);
  } else {
    float val_array[] = {pres, gas_res, a_temp, a_hum, gd_temp, gd_hum};
    int n = sizeof(val_array)/sizeof(float);

    Serial.print(id);
    Serial.print(" ");
    for (int i=0; i<n; i++){
      Serial.print(val_array[i]);
      Serial.print(" ");
    }
    Serial.println();
  }
}
