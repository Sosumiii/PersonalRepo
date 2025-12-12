int trigPIN = 7;
int echoPIN = 8;
int LEDPIN = 13;
long echoVal;
long echoDist;
long dist;

long distCalc(){
    echoVal = pulseIn(echoPIN, HIGH);
    echoDist = echoVal / 58;

    return echoDist;
}

void setup()
{
    pinMode(trigPIN, OUTPUT);
    pinMode(echoPIN, INPUT);
    pinMode(LEDPIN, OUTPUT);

    //Serial.begin(9600);

}

void loop()
{
    digitalWrite(trigPIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPIN, LOW);

    dist = distCalc();
    //Serial.print("Distance: ");
    //Serial.println(dist);

    if (dist < 10){
        digitalWrite(LEDPIN, HIGH);
    } else{
        digitalWrite(LEDPIN, LOW);
    }

    delay(10);
	
}
