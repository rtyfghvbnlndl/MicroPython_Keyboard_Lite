class passwd_ctrl(object):
    def __init__(self, passwd_dict):
        if not passwd_dict:
            raise ValueError
        self.passwd_list = list(passwd_dict.values())
        self.id_list = list(passwd_dict.keys())
        self.index = -1
        self.len=len(self.id_list)

    def next(self):
        if self.index<self.len-1:
            self.index+=1
        else:
            self.index=0
        id, passwd = self.id_list[self.index], self.passwd_list[self.index]
        return id, passwd
    
    def last(self):
        if self.index>0:
            self.index-=1
        else:
            self.index=self.len-1
        id, passwd = self.id_list[self.index], self.passwd_list[self.index]
        return id, passwd

def passwd_keyboard(oled, keyboard, output):
    passwd_dict = {
        'ID1':'ahgdshdoahdoahscoaugcbaiuidgia698o',
        'ID2':'ahg',
        'ID3':'',
        'ID4':'chsdijduhsgydfy'
    }
    import effect
    from time import sleep
    ps = passwd_ctrl(passwd_dict)
    
    name, passwd = ps.next()
    pd_generator = effect.next_index(passwd, 15)
    oled.text(name, 0, 8)
    oled.show()

    while True:
        code = keyboard.scan_code()
        sleep(0.1)
        
        to_show, num =next(pd_generator)

        oled.fill_rect(0, 0, 127, 7, 0)
        oled.fill_rect(0, 16, 127, 23, 0)
        oled.text(str(code), 0, 0)
        oled.text(to_show, 0, 16)
        oled.show()

        if 12 in code:
            while 12 in keyboard.scan_code():
                pass
            name, passwd = ps.next()
            oled.fill_rect(0, 8, 127, 31, 0)
            oled.text(name, 0, 8)
            pd_generator = effect.next_index(passwd, 15)
            oled.show()

        elif 8 in code:
            while 8 in keyboard.scan_code():
                pass
            name, passwd = ps.last()
            oled.fill_rect(0, 8, 127, 31, 0)
            oled.text(name, 0, 8)
            pd_generator = effect.next_index(passwd, 15)
            oled.show()
        
        elif 4 in code:
            while 4 in keyboard.scan_code():
                pass
            output.write(passwd.encode('ascii'))
            oled.fill_rect(0, 24, 127, 31, 0)
            oled.text('done!', 0, 24)
            oled.show()
        
        elif 9 in code:
            while 9 in keyboard.scan_code():
                pass
            break