void setup() {
  pinMode(10, OUTPUT);   
  Serial.begin(9600);
}
char c;
void loop() {
  c=Serial.read();
  if (c=='a') digitalWrite(10,HIGH);
  else if (c=='s') digitalWrite(10,LOW);
  else if (c=='d') Serial.write("selamat datang");
}
