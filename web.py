
def web(oled, keyboard, np):
    from microdot import Microdot
    import network, time

    for i in range(15):
       np[i]=(0,0,0)
    np.write()

    def do_connect(wlan,ssid, passwd):
        wlan.active(True)
        if not wlan.isconnected():
            print('connecting to network...')
            if not wlan or not passwd:
                return False
            wlan.connect(ssid, passwd)
            for i in range(30):
                if wlan.isconnected():
                    return True
                else:
                    time.sleep(0.5)
            else:
                return False

    def webserver(wlan):
        ap = network.WLAN(network.AP_IF) 
        ap.config(essid='ESP32_AP')
        ap.active(True)

        app = Microdot()

        @app.route('', methods=['GET', 'POST'])
        def index(req):
            with open('index.html', mode='r', encoding='utf-8') as html:
                return html.read(), 200, {'Content-Type': 'text/html'}
        
        @app.route('exit', methods=['GET', 'POST'])
        def exit_now(req):
            req.app.shutdown()
            return 'exit!'
            
        @app.route('wifi', methods=['GET', 'POST'])
        def wifi(req):
            ssid, passwd = None, None
            if req.method == 'POST':
                ssid = req.form.get('ssid')
                passwd = req.form.get('passwd')
                print(123,ssid,passwd)

                if do_connect(wlan,ssid,passwd):
                    req.app.shutdown()
                    return 'success'
        
            with open('wifi.html', mode='r', encoding='utf-8') as html:
                return html.read(), 200, {'Content-Type': 'text/html'}
            
        @app.route('passwd', methods=['GET', 'POST'])
        def passwd(req):
            if req.method == 'POST':
                with open('passwd_dict', mode='r', encoding='utf-8') as f:
                    pdict = eval(f.read())
                name = req.form.get('name')
                passwd = req.form.get('passwd')
                try:
                    exist = int(req.form.get('save'))
                except:
                    exist = 1
                print(name,passwd,exist)
                if exist:
                    pdict[name]=passwd
                else:
                    pdict.pop(name)
                with open('passwd_dict', mode='w+', encoding='utf-8') as f:
                    f.write(str(pdict))#oled

            with open('passwd.html', mode='r', encoding='utf-8') as html:
                return html.read(), 200, {'Content-Type': 'text/html'}
        
        @app.route('value', methods=['GET', 'POST'])
        def value(req):
            with open('passwd_dict', mode='r', encoding='utf-8') as f:
                pdict = eval(f.read())
                xml='<a>'
                for key,value in pdict.items():
                    xml+='<object><name>%s</name><passwd>%s</passwd></object>' % (key,value)
                xml+='</a>'
                return xml, 200, {'Content-Type': 'text/xml'}

        app.run(port=80)
        return ap

    oled.fill(0)
    oled.text('setting mode ',0,0)
    oled.text('press key8 ',0,8)
    oled.show()

    wlan = network.WLAN(network.STA_IF)
    while True:
        code = keyboard.scan_code()
        if 8 in code:
            while 8 in keyboard.scan_code():
                pass
            oled.fill(0)
            oled.text('connect to wifi ',0,0)
            oled.text('ESP32_AP ',0,8)
            oled.text('open webpage',0,16)
            oled.text('192.168.4.1 ',0,24)
            oled.show()
            ap=webserver(wlan)
            ap.active(False)
        elif 3 in code:
            while 3 in keyboard.scan_code():
                pass
            oled.fill(0)
            break
        time.sleep(0.15)


if __name__ == '__main__':
    import py_keyboard   
    from neopixel import NeoPixel
    from machine import Pin, I2C, UART, PWM
    import ssd1306
    i2c = I2C(scl=Pin(2), sda=Pin(3))
    oled = ssd1306.SSD1306_I2C(128,32,i2c)
    keyboard = py_keyboard.keyboard([0,1,6,7,5],[9,8,4])
    np = NeoPixel(Pin(10 , Pin.OUT), 16)
    web(oled, keyboard, np)