import py_keyboard, time
from neopixel import NeoPixel
from machine import Pin, I2C
import ssd1306

keyboard = py_keyboard.keyboard((0,1,6,7),(9,8,4,5))

i2c = I2C(scl=Pin(2), sda=Pin(3))
oled = ssd1306.SSD1306_I2C(128,32,i2c)

oled.fill(0)
oled.rotate(False)
oled.text('HELLO.', 0, 0)
oled.text('keyboard.', 0, 8)
oled.show()

print('keyboard_size:%ix%i' % (keyboard.out_length,keyboard.in_length))

pin = Pin(10 , Pin.OUT)   
np = NeoPixel(pin, 16)
for i in range(16):  
    np[i] = (8*i+64, 256-8*i, 8*i+64) 
np.write()     

while True:
    L0 = keyboard.scan_single(0)
    print(L0)

    all = keyboard.scan()
    print(all)

    code = keyboard.scan_code()
    print(code)
    time.sleep(0.05)

    oled.fill_rect(0, 16, 127, 24, 0)
    oled.text(str(code), 0, 16)
    oled.show()