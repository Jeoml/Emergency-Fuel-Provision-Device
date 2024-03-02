trigPin = 10;
echoPin = 9;
void setup()
{

  Serial.begin(9600); 
  delay(100);
 PinMode(trigPin,OUTPUT);
 PinMode(echoPin,OUTPUT);
}


void loop()
{
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  
  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);
  
  // Calculate the distance
  distanceCm = duration *
 if (distanceCm < 5)
{
  if (Serial.available()>0)
   switch(Serial.read())
  {
    case 's':
      SendMessage();
      break;
    case 'r':
      break;
  }

}
 if (mySerial.available()>0)  Serial.write(mySerial.read());
}


 void SendMessage()
{
  mySerial.println("AT+CMGF=1");    //Sets the GSM Module in Text Mode
  delay(1000);  // Delay of 1000 milli seconds or 1 second
  mySerial.println("AT+CMGS=\"+9178931422x0\"\r"); // Replaing with mobile number
  delay(1000);
  mySerial.println("I am SMS from GSM Module");// The SMS text to send
  delay(100);
   mySerial.println((char)26);// ASCII code of CTRL+Z
  delay(1000);
}
