#define echo 2
#define trigger 3

#define RLED 12
#define GLED 13
#define YLED 10
#define buzzer 11


long echoVal;
long echoDist;
long dist;

long distCalc(){
    echoVal = pulseIn(echo, HIGH);
    echoDist = echoVal / 58;

    return echoDist;
}

void setup()
{
	pinMode(RLED, OUTPUT);
    pinMode(GLED, OUTPUT);
    pinMode(YLED, OUTPUT);
    pinMode(buzzer, OUTPUT);

    pinMode(trigger, OUTPUT);
    pinMode(echo, INPUT);
    Serial.begin(9600);
}

void loop()
{
	digitalWrite(trigger, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigger, LOW);

    dist = distCalc();
    Serial.print("Distance: ");
    Serial.println(dist);

    if (dist < 8){
        digitalWrite(RLED, HIGH);
        digitalWrite(GLED, LOW);
        digitalWrite(YLED, LOW);
        tone(buzzer, 2000);
    }

    else if (dist < 20 && dist >= 9){
        digitalWrite(RLED, LOW);
        digitalWrite(GLED, LOW);
        digitalWrite(YLED, HIGH);
        tone(buzzer, 1000);
    } 

    else {
        digitalWrite(RLED, LOW);
        digitalWrite(GLED, HIGH);
        digitalWrite(YLED, LOW);
        noTone(buzzer);
    }

    delay(250);
}
