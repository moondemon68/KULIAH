void setup() {
  pinMode(10, OUTPUT);     //Menjadikan pin lampu (pin 10) sebagai output.
}

void loop() {
  digitalWrite(10,HIGH);   //Menyalakan lampu
  delay(500);                //Lampu menyala selama 500 milidetik
  digitalWrite(10,LOW);    //Mematikan lampu
  delay(500);                //Lampu mati selama 500 milidetik
}
