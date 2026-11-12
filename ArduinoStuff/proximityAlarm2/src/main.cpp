#include <Arduino.h>
#include <Adafruit_VL53L0X.h>

#define GLED_PIN 18
#define RLED_PIN 19
#define BUZZER 25

//#define TOFSCL_PIN 22
//#define TOFSDA_PIN 21

Adafruit_VL53L0X sensor = Adafruit_VL53L0X();
int dist;

void setup() {
  // put your setup code here, to run once:
  pinMode(GLED_PIN, OUTPUT);
  pinMode(RLED_PIN, OUTPUT);
  pinMode(BUZZER, OUTPUT);


  Serial.begin(9600);

  
  delay(500); // wait for serial port to connect. Needed for native USB
  

  Serial.println("Adafruit VL53L0X test");

  if (!sensor.begin()) {
    Serial.println("Failed to boot VL53L0X");
    while (1);
  }

  sensor.startRangeContinuous();
}

void loop() {
  // put your main code here, to run repeatedly:
  if (sensor.isRangeComplete()) {    
    dist = sensor.readRange();

    if (dist < 400 && dist > 200) {
      digitalWrite(RLED_PIN, LOW);
      digitalWrite(GLED_PIN, HIGH);

      tone(BUZZER, 1000);
      delay(200);

      digitalWrite(GLED_PIN, LOW);
      noTone(BUZZER);
      delay(200);

    }

    else if (dist < 200 && dist > 100){
      digitalWrite(RLED_PIN, LOW);      
      digitalWrite(GLED_PIN, HIGH);

      tone(BUZZER, 1000);
      delay(50);

      digitalWrite(GLED_PIN, LOW);
      noTone(BUZZER);
      delay(50);

    }

    else if (dist < 100){
      digitalWrite(RLED_PIN, HIGH);
      tone(BUZZER, 1000);
      digitalWrite(GLED_PIN, LOW);
    }

    else{
      digitalWrite(GLED_PIN, HIGH);
      noTone(BUZZER);
      digitalWrite(RLED_PIN, LOW);
    }

    
    Serial.print("Distance in mm: ");
    Serial.println(dist);
  }

}

