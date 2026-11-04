import time
from machine import I2C, Pin
import bme280_float

# Define I2C port and pins (I2C0 using GP4 for SDA and GP5 for SCL)
I2C_ID = 0
PIN_SDA = 4
PIN_SCL = 5

BME280_ADDR = 0x76
MLX90614_ADDR = 0x5a

print("----------------------------------------")
print("Pico 2W Temperature and humidity checks")
print("----------------------------------------")

# Initialize I2C bus and give error if it was hooked up wrong
try:
  i2c = I2C(I2C_ID, sda=Pin(PIN_SDA), scl=Pin(PIN_SCL), freq=100000)
  print(f"[I2C] Initialized I2C{I2C_ID} on SDA: GP{PIN_SDA}, SCL: GP{PIN_SCL}")
except Exception as e:
  print(f"[ERROR] Failed to initialize I2C: {e}")
  i2c = None

print("Initializing BME280 sensor...")
try:
  # Reference the float module when instantiating the class
  bme = bme280_float.BME280(i2c=i2c)
  print("[SUCCESS] BME280 initialized successfully!")
except Exception as e:
  print(f"[ERROR] Could not initialize BME280: {e}")
  bme = None

try:
  while True:
    if bme:
      # Pull live temperature, pressure, and humidity float values
      temp, pressure, humidity = bme.values
      print(f"Humidity: {humidity}  |  Temperature: {temp}  |  Pressure: {pressure}")
    else:
      print("Sensor not available. Check wiring.")

    time.sleep(2)

except KeyboardInterrupt:
  print("\nTest stopped.")
