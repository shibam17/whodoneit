#include <IRremote.h>

//Define Pins
int Led = 10;
int buzzer = 9;
int RECV_PIN = 11;
//IR Library stuff

IRrecv irrecv(RECV_PIN);
decode_results results;


void setup()
{
  //Set Led Pins
  pinMode(Led, OUTPUT);
  pinMode(buzzer, OUTPUT);

  //Enable serial usage and IR signal in
  Serial.begin(9600);
  Serial.println("Enabling IRin");
  irrecv.enableIRIn(); 
  Serial.println("Enabled IRin");
}

void loop() {
  if (irrecv.decode(&results)) {//irrecv.decode(&results) returns true if anything is recieved, and stores info in varible results
    unsigned int value = results.value; //Get the value of results as an unsigned int, so we can use switch case
    Serial.println(value);
    if ( value == 65535 || value == 12495){
      digitalWrite(Led, HIGH);
      tone(buzzer, 1000); 
       delay(1000);
       noTone(buzzer);
       digitalWrite(Led, LOW);
    }
    irrecv.resume(); // Receive the next value
  }
}
