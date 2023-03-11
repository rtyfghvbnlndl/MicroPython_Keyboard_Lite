import py_keyboard
from neopixel import NeoPixel
from machine import Pin, I2C, UART, PWM
import ssd1306
from time import sleep

keyboard = py_keyboard.keyboard((0,1,6,7),(9,8,4,5))

i2c = I2C(scl=Pin(2), sda=Pin(3))
oled = ssd1306.SSD1306_I2C(128,32,i2c)
buzz = PWM(Pin(13), duty=0, freq=1000)
buzz.duty(1)
sleep(0.3)
buzz.duty(0)

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

import passwd_keyboard, web, piano, autopiano

while True: 
    passwd_keyboard.passwd_keyboard(oled,keyboard,output,np)
    web.web(oled, keyboard,np)
    piano.piano(buzz, keyboard, oled, np)
    autopiano.piano(buzz, keyboard, oled, np)
    


