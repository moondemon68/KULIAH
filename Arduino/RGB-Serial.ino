int red=4,blue=6,green=5;
int r=0,g=0,b=0;
void setup() {
  // put your setup code here, to run once:
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  Serial.begin(9600);
  digitalWrite(red,HIGH);
  digitalWrite(blue,HIGH);
  digitalWrite(green,HIGH);
}
char c;
void loop() {
  // put your main code here, to run repeatedly:
  c=Serial.read();
  if (c=='r') {
    if (!r) digitalWrite(red,LOW);
    else digitalWrite(red,HIGH);
    r=1-r;
    Serial.print(r);
    Serial.print(g);
    Serial.print(b);
    Serial.println();
  }
  if (c=='b') {
    if (!b) digitalWrite(blue,LOW);
    else digitalWrite(blue,HIGH);
    b=1-b;
    Serial.print(r);
    Serial.print(g);
    Serial.print(b);
    Serial.println();
  }
  if (c=='g') {
    if (!g) digitalWrite(green,LOW);
    else digitalWrite(green,HIGH);
    g=1-g;
    Serial.print(r);
    Serial.print(g);
    Serial.print(b);
    Serial.println();
  }
  if (c=='x') {
    digitalWrite(red,HIGH);
    digitalWrite(blue,HIGH);
    digitalWrite(green,HIGH);
    r=0;
    b=0;
    g=0;
    Serial.print(r);
    Serial.print(g);
    Serial.print(b);
    Serial.println();
  }
}
