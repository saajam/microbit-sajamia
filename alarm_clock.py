# Write your code here :-)
from microbit import *
from ultrasonic import Ultrasonic
from ssd1306 import initialize, clear_oled
from ssd1306_text import add_text


ultrasonic_sensor = Ultrasonic()
initialize()
clear_oled()

while True:
    distance_value = ultrasonic_sensor.measure_distance_cm()
    motion = pin2.read_digital()

    add_text(0, 0, str(distance_value))

    if distance_value <= 20:
        if motion == 1:
            add_text(0, 1, 'motion detected')

            pin1.write_digital(1)
            pin0.write_digital(1)
        else:
            add_text(0, 1, 'no motion')

            pin1.write_digital(0)
            pin0.write_digital(0)
