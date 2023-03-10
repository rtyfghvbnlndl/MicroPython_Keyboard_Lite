import py_keyboard
from neopixel import NeoPixel
from machine import Pin, I2C, UART
import ssd1306
from time import sleep

keyboard = py_keyboard.keyboard((0,1,6,7),(9,8,4,5))

i2c = I2C(scl=Pin(2), sda=Pin(3))
oled = ssd1306.SSD1306_I2C(128,32,i2c)

oled.fill(0)
oled.rotate(False)
oled.text('keyboard.', 24, 8)
oled.show()
sleep(1)
oled.fill(0)
oled.show()

print('keyboard_size:%ix%i' % (keyboard.out_length,keyboard.in_length))

np = NeoPixel(Pin(10 , Pin.OUT), 16)
output = UART(1, baudrate=9600, tx=20, rx=21)

for i in range(16):  
    np[i] = (8*i+64, 256-8*i, 8*i+64) 
np.write()     

import passwd_keyboard, web

while True:
    passwd_keyboard.passwd_keyboard(oled,keyboard,output)
    web.web(oled, keyboard)
