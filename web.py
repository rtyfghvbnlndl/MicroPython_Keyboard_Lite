
def web(oled, keyboard):
    from microdot import Microdot
    import network, time
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

    def connet_by_webserver(wlan):
        ap = network.WLAN(network.AP_IF) 
        ap.config(essid='ESP32_AP')
        ap.active(True)

        app = Microdot()

        @app.route('', methods=['GET', 'POST'])
        def index(req):
            global try_connect
            ssid, passwd = None, None
            if req.method == 'POST':
                ssid = req.form.get('ssid')
                passwd = req.form.get('passwd')
                print(123,ssid,passwd)

                if do_connect(wlan,ssid,passwd):
                    req.app.shutdown()
                    return 'success'
                else:
                    try_connect=True
        
            with open('index.html', mode='r', encoding='utf-8') as html:
                if not try_connect:
                    status = ' '
                else:
                    status = '<div class="fail">Wifi Connection Failed.</div>'
                return f'%s{status}' % html.read(), 200, {'Content-Type': 'text/html'}

        app.run(port=80)
        return ap

    oled.fill(0)
    oled.text('connect ',0,0)
    oled.show()

    wlan = network.WLAN(network.STA_IF)
    try_connect = False
    while True:
        code = keyboard.scan_code()
        if not wlan.isconnected() and 8 in code:
            while 8 in keyboard.scan_code():
                pass
            ap=connet_by_webserver(wlan)
            ap.active(False)
        elif 9 in code:
            while 9 in keyboard.scan_code():
                pass
            break
        time.sleep(0.15)
