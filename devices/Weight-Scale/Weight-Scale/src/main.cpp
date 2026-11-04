#include <Arduino.h>
#include <HX711.h>

// Define ESP32 pins connected to HX711
const int DT_PIN = 23;
const int SCK_PIN = 22;

HX711 scale;
bool isStreaming = true;

void setup() {
  Serial.begin(115200);
  delay(1000);
  
  Serial.println("\n[INIT] Initializing HX711 Load Cell via PlatformIO...");
  scale.begin(DT_PIN, SCK_PIN);

  // Set initial scale factor (update this after calibration)
  scale.set_scale(46.51f); 

  Serial.println("[INFO] Taring scale... Please keep the platform completely empty.");
  scale.tare(); // Zero out the scale
  Serial.println("[SUCCESS] Scale tared and ready!");
  Serial.println("\n--- Serial Controls ---");
  Serial.println("  [t] -> Tare the scale");
  Serial.println("  [s] -> Start / Stop telemetry stream\n");
}
void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();

    if (cmd != '\n' && cmd != '\r') {
      if (cmd == 't' || cmd == 'T') {
        Serial.println("\n[CMD] Taring scale...");
        scale.tare();
        Serial.println("[SUCCESS] Scale tared successfully!");
      } 
      else if (cmd == 's' || cmd == 'S') {
        isStreaming = !isStreaming;
        Serial.print("\n[CMD] Telemetry stream is now: ");
        Serial.println(isStreaming ? "RESUMED (Active)" : "PAUSED (Stopped)");
      }
    }
  }

  // Only read and print weight if streaming is active
  if (isStreaming) {
    if (scale.is_ready()) {
      float weightGrams = scale.get_units(5);
      float weightLbs = weightGrams / 453.592f;
      // Apply a small deadzone filter to lock tiny noise to 0.00 g
      if (abs(weightLbs) < 0.10) {
        weightLbs = 0.0;
      }
      Serial.print("Current Weight: ");
      Serial.print(weightLbs, 2);
      Serial.println(" g");
    } else {
      Serial.println("[WARNING] HX711 sensor not responding.");
    }
  }
  delay(500); // Prevents the ESP32 watchdog timer from triggering a reset
}