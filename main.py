import py_keyboard   
from neopixel import NeoPixel
from machine import Pin, I2C, UART, PWM
import ssd1306
from time import sleep
object
class ssd1306_(ssd1306.SSD1306_I2C):
    no_reponse = 0
    max_no_reponse = 200
    def timer_run(self):
        if self.no_reponse<=self.max_no_reponse:
            self.no_reponse+=1
    
    def reset_timer(self):
        self.no_reponse=0
    
    def screen_sleep(self):
        if self.no_reponse>self.max_no_reponse:
            self. poweroff()
        else:
            self.poweron()


keyboard = py_keyboard.keyboard([0,1,6,7,5],[9,8,4])

i2c = I2C(scl=Pin(2), sda=Pin(3))
oled = ssd1306_(128,32,i2c)
buzz = PWM(Pin(13), duty=0, freq=1000)
buzz.duty(1)
sleep(0.3)
buzz.duty(0)

oled.fill(0)
oled.rotate(False)
oled.text('Beta version', 10, 8)
oled.show()
sleep(1)
oled.fill(0)
oled.show()

print('keyboard_size:%ix%i' % (keyboard.out_length,keyboard.in_length))

np = NeoPixel(Pin(10 , Pin.OUT), 16)
output = UART(1, baudrate=9600, tx=20, rx=21)
import passwd_keyboard, web, piano, autopiano,numberkeyboard

while True: 
    numberkeyboard.board(keyboard,np,output,oled)
    passwd_keyboard.passwd_keyboard(oled,keyboard,output,np)
    piano.piano(buzz, keyboard, oled, np)
    #autopiano.piano(buzz, keyboard, oled, np)
    web.web(oled, keyboard,np)
    


