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

def passwd_keyboard(oled, keyboard, output, np):
    oled.reset_timer()

    for i in range(15):  
        np[i] = (8*i+64, 256-8*i, 8*i+64) 
    np.write() 
    with open("passwd_dict","r",encoding="utf-8") as f:
        passwd_dict = eval(f.read())
    import effect
    from time import sleep
    ps = passwd_ctrl(passwd_dict)
    
    name, passwd = ps.next()
    pd_generator = effect.next_index(passwd, 15)
    oled.text(name, 0, 8)
    oled.show()

    while True:
        oled.screen_sleep()
        code = keyboard.scan_code()
        
        to_show, num =next(pd_generator)

        oled.fill_rect(0, 0, 127, 7, 0)
        oled.fill_rect(0, 16, 127, 23, 0)
        oled.text(str(code), 0, 0)
        oled.text(to_show, 0, 16)
        oled.show()

        if code:
            if 14 in code:
                while 14 in keyboard.scan_code():
                    pass
                name, passwd = ps.next()
                oled.fill_rect(0, 8, 127, 31, 0)
                oled.text(name, 0, 8)
                pd_generator = effect.next_index(passwd, 15)
                oled.show()

            elif 4 in code:
                while 4 in keyboard.scan_code():
                    pass
                name, passwd = ps.last()
                oled.fill_rect(0, 8, 127, 31, 0)
                oled.text(name, 0, 8)
                pd_generator = effect.next_index(passwd, 15)
                oled.show()
            
            elif 9 in code:
                while 9 in keyboard.scan_code():
                    pass
                iteractor = iter(passwd)
                while True:
                    sleep(0.1)
                    try:
                        char = next(iteractor)
                    except StopIteration:
                        break
                    if char == '$':
                        char_cache = '$'
                        for key_char in 'enter':
                            char = next(iteractor) 
                            char_cache += char
                            if char == key_char:
                                pass
                            else:
                                break
                        else:
                            output.write(b'\x1B')
                            continue
                        char = char_cache
                    output.write(char.encode('ascii'))
                    
                oled.fill_rect(0, 24, 127, 31, 0)
                oled.text('done!', 0, 24)
                oled.show()
            
            elif 3 in code:
                while 3 in keyboard.scan_code():
                    pass
                oled.fill(0)
                break
            oled.reset_timer()
        else:
            oled.timer_run()
        sleep(0.1)

if __name__ == '__main__':
    from time import sleep
    from machine import UART
    output = UART(1, baudrate=9600, tx=20, rx=21)
    sleep(2)
    iteractor = iter('#include <iostream>$enterusing namespace std;$enterint main()$enter{$enter    cout << "Hello, world!" << "\\n";$enter    return 0;$enter')
    while True:
        sleep(0.1)
        try:
            char = next(iteractor)
        except StopIteration:
            break
        if char == '$':
            char_cache = '$'
            for key_char in 'enter':
                char = next(iteractor) 
                char_cache += char
                if char == key_char:
                    pass
                else:
                    break
            else:
                output.write(b'\x1B')
                continue
            char = char_cache
        output.write(char.encode('ascii'))