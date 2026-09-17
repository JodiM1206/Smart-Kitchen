import time 
import mlx90614
from machine import I2C, Pin

i2c = I2C(0, scl=Pin(5), sda=Pin(4), freq=100000)
sensor = mlx90614.MLX90614(i2c)

while True:
    print(sensor.read_ambient_temp(),sensor.read_object_temp())
    time.sleep_ms(500)


