#include <Arduino.h>
#line 1 "/home/sosumi/Documents/Github/PersonalRepo/ArduinoStuff/thermometer/thermometer.ino"
#include "DHT.h"
#define DHTPIN 13      // Pin where the DATA line is connected
#define DHTTYPE DHT11 // Sensor type

double lastTemp = -1000;
double temperature;

DHT dht(DHTPIN, DHTTYPE);

#line 10 "/home/sosumi/Documents/Github/PersonalRepo/ArduinoStuff/thermometer/thermometer.ino"
void setup();
#line 16 "/home/sosumi/Documents/Github/PersonalRepo/ArduinoStuff/thermometer/thermometer.ino"
void loop();
#line 10 "/home/sosumi/Documents/Github/PersonalRepo/ArduinoStuff/thermometer/thermometer.ino"
void setup()
{
    dht.begin();
    Serial.begin(115200);
}

void loop()
{
    delay(2000);  // DHT11 requires ~1–2 seconds between reads

    float temp = dht.readTemperature(true); // true = Fahrenheit

    if (!isnan(temp) && temp != lastTemp) {
        lastTemp = temp;
        Serial.println(temp);
    }

