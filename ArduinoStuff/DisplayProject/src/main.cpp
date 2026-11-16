#include <Arduino.h>
#include <LiquidCrystal.h>

LiquidCrystal lcd(32, 33, 25, 26, 27, 14);

void setup() {
    delay(100);

    Serial.begin(115200);

    lcd.begin(16, 2);

    lcd.setCursor(0, 0);
    lcd.print("Hello World!");

    lcd.setCursor(0, 1);
    lcd.print("LCD Tutorial");

    delay(5000);

    lcd.clear();

    lcd.setCursor(0,0);

    for(int i = 4; i >= 0; i--) {
      lcd.print(i);
      delay(1000);
      lcd.clear();
    }

}

void loop() {
  lcd.print("Ding Ding Ding!");
  delay(500);
  
  lcd.clear();
  delay(500);

}