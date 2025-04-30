import max7219
from machine import Pin, SPI, ADC
import time

spi = SPI(1, baudrate=10000000, polarity=1, phase=0, sck=Pin(4), mosi=Pin(6))
cs = Pin(7, Pin.OUT)
display = max7219.Matrix8x8(spi, cs, 1)

display.brightness(10)

pot = ADC(Pin(0))
pot.atten(ADC.ATTN_11DB)

display.fill(0)
display.show()

while True:
    pot_value = pot.read()
    num_leds = int((pot_value / 4095) * 32) # Scale to 0-32

    display.fill(0)

    led_count = 0
    for row in range(8):
        for col in range(8):
            if led_count <= num_leds:
                display.pixel(col, row, 1)
                led_count += 1
            else:
                break

    display.show()
    time.sleep(0.1)
