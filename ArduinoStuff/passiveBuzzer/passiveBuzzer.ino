#define buzzer 5

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
