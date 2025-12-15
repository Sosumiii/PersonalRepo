#include <Arduino.h>
#line 1 "/home/sosumi/Documents/Github/PersonalRepo/ArduinoStuff/passiveBuzzer/passiveBuzzer.ino"
#define buzzer 5

#line 3 "/home/sosumi/Documents/Github/PersonalRepo/ArduinoStuff/passiveBuzzer/passiveBuzzer.ino"
void setup();
#line 8 "/home/sosumi/Documents/Github/PersonalRepo/ArduinoStuff/passiveBuzzer/passiveBuzzer.ino"
void loop();
#line 3 "/home/sosumi/Documents/Github/PersonalRepo/ArduinoStuff/passiveBuzzer/passiveBuzzer.ino"
void setup()
{
    pinMode(buzzer, OUTPUT);
}

void loop()
{
	tone(buzzer, 482);
    delay(1000);
    noTone(buzzer);
    delay(1000);
    
}

