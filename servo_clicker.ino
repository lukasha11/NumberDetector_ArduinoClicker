#include <Servo.h>

Servo myServo;
int angle = 90;
int numRotations = 0;

void setup() {
  Serial.begin(9600);
  myServo.attach(9); // Podłącz serwomechanizm do pinu 9
}

void loop() {
  if (Serial.available() > 0) {
    numRotations = Serial.parseInt(); // Wczytaj liczbę obrotów ze Serial Monitora

    for (int i = 0; i < numRotations; i++) {
      // Obróć serwomechanizm o 30 stopni w jednym kierunku
      for (angle = 90; angle <= 115; angle += 1) {
        myServo.write(angle);
        delay(2);
      }

      delay(50); // Poczekaj 1 sekundę

      // Obróć serwomechanizm o 30 stopni w drugim kierunku
      for (angle = 115; angle >= 90; angle -= 1) {
        myServo.write(angle);
        delay(2);
      }

      delay(50); // Poczekaj 1 sekundę
    }
  }
}
