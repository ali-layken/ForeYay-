char inByte;
void setup(){
  #define red 7
  #define green 11
  #define blue 5
  analogWrite(red, 0);
  analogWrite(blue, 0);
  analogWrite(green, 0);
  Serial.begin(9600);
}

void loop() {
  inByte = (char) Serial.read();
   switch (inByte) {
      case 'r':
        analogWrite(red, 255);
        break;
      case 'g':
        analogWrite(green, 255);
        break;
      case 'b':
        analogWrite(blue, 255);
        break;
      case 'p':
        analogWrite(red, 255);
        analogWrite(blue, 255);
        break;
      case 'y':
        analogWrite(red, 255);
        analogWrite(green, 100);
        break;
      case 't':
        analogWrite(green, 255);
        analogWrite(blue, 255);
        break;
      case 'w':
        analogWrite(blue, 255);
        analogWrite(red, 255);
        analogWrite(green, 255);
        break;
      case 'o':
        analogWrite(blue, 0);
        analogWrite(red, 0);
        analogWrite(green, 0);
        break;
   }
 }
