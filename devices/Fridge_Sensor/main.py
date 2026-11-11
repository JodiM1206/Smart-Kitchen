from machine import Pin, SPI, I2C
import st7789py as st7789
import bme280_float
import vga2_8x16 as font
import time

# 1. Initialize I2C1 for BME280 sensor (SDA: GP14, SCL: GP15)
i2c = I2C(1, sda=Pin(14), scl=Pin(15), freq=800000)
bme = bme280_float.BME280(i2c=i2c)

# 2. Initialize SPI0 for ST7789 display (SCK: GP2, MOSI: GP3)
spi = SPI(0, baudrate=60000000, polarity=0, phase=0,
          sck=Pin(2), mosi=Pin(3))

# 3. Initialize ST7789 display (DC: GP4, RES: GP0, CS: GP1)
# Backlight is wired directly to 3.3V (always on)
tft = st7789.ST7789(
    spi,
    240, 240,
    reset=Pin(0, Pin.OUT),
    cs=Pin(1, Pin.OUT),
    dc=Pin(4, Pin.OUT),
    rotation=0
)

tft.fill(st7789.BLACK)

tft.text(font, "Fridge Sensor", 20, 20, st7789.CYAN, st7789.BLACK)

# 4. Main loop to read sensor and update display
while True:
    try:
        temp, pressure, humidity = bme.values
        print(f"Temp: {temp} | Humidity: {humidity}")

        # Clear and update only the Temperature line region (x=20, y=70, width=200, height=16)
        tft.fill_rect(20, 70, 200, 16, st7789.BLACK)
        tft.text(font, f"Temp: {temp}", 20, 70, st7789.WHITE, st7789.BLACK)

        # Clear and update only the Humidity line region (x=20, y=110, width=200, height=16)
        tft.fill_rect(20, 110, 200, 16, st7789.BLACK)
        tft.text(font, f"Humidity: {humidity}", 20, 110, st7789.WHITE, st7789.BLACK)

    except Exception as e:
        print("Error reading sensor:", e)
        tft.fill_rect(20, 70, 200, 16, st7789.BLACK)
        tft.text(font, "Sensor Error", 20, 70, st7789.RED, st7789.BLACK)

    time.sleep(2)
