from machine import Pin

class keyboard(object):

    def __init__(self, in_low = [], out_high = []):
        self.IN = []
        self.OUT = []
        for i in in_low:
            self.IN.append(Pin(i,mode=Pin.IN, pull=Pin.PULL_DOWN))
        for i in out_high:
            self.OUT.append(Pin(i, mode=Pin.OUT, value=0))
        
        self.out_length=len(self.OUT)
        self.in_length=len(self.IN)
    
    def scan_single(self, OUT_code):
        self.OUT[OUT_code].value(1)
        output = []
        for i in self.IN:
            output.append(i.value())
        self.OUT[OUT_code].value(0)
        return output
    
    def scan(self):
        output = []
        for i in range(self.out_length):
            output.append(self.scan_single(i))
        return output
    
    def scan_code(self):
        key_list = self.scan()
        output = []
        for x, x_val in enumerate(key_list):
            for y, y_val in enumerate(x_val):
                if y_val:
                    output.append(x*self.in_length+y)
        return output
    
if __name__ == '__main__':
    from time import sleep
    a=keyboard([0,1,6,7,5],[9,8,4])
    from neopixel import NeoPixel
    np = NeoPixel(Pin(10 , Pin.OUT), 16)
    for i in range(16):
        np[i]=(2,3,4)
    while True:
        sleep(0.3)
        print(a.scan(),a.scan_code())


