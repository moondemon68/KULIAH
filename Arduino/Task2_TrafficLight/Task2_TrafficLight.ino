int g=4,y=3,r=2;
void setup() {
  // put your setup code here, to run once:
  pinMode(g,OUTPUT);
  pinMode(y,OUTPUT);
  pinMode(r,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(g,HIGH);
  delay(3000);
  digitalWrite(g,LOW);
  digitalWrite(y,HIGH);
  delay(1000);
  digitalWrite(y,LOW);
  digitalWrite(r,HIGH);
  delay(3000);
  digitalWrite(r,LOW);
}
