void setup() {
  pinMode(10, OUTPUT);     //Menjadikan pin lampu (pin 10) sebagai output.
}

void loop() {
  digitalWrite(10,HIGH);   //Menyalakan lampu
  delay(1000);                //Lampu menyala selama 1 detik
  digitalWrite(10,LOW);    //Mematikan lampu
  delay(1000);                //Lampu mati selama 1 detik
}
