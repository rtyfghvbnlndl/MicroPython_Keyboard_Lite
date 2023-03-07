def next_index(text=str, display_length=int):
    iterable_text = iter(text)
    num = 0
    while True:
        to_show = list(' ' * display_length)
        while True:
            try:
                to_show[num] = next(iterable_text)
            except StopIteration:
                break
            if num < display_length - 1:
                num += 1
            else:
                num = 0
            to_show[num] = '_'
            yield to_show, num

passwd_dict = {
    'aaaa':'ahgdshdoahdoahscoaugcbaiuidgia698o',
    'bbb':'ahg',
    'cc':'',
    'dd':'chsdijduhsgydfy'
}

def passwd_keyboard(display, keyboard):
    import time

    def for_dict(dict):
        while True:
            b = iter(dict)
            while True:
                try:    
                    name = next(b)
                    passwd = dict[name]
                    yield name, passwd
                except StopIteration:
                    break
    iterable_b = for_dict(passwd_dict)

    name, passwd = next(iterable_b)
    iterable_a = next_index(passwd, 15)
    while True:
        try:
            keyboard.code().index(8)
            
            name, passwd = next(iterable_b)
            iterable_a = next_index(passwd, 15)
        except ValueError:
            pass
        try:
            keyboard.code().index(4)
            time.sleep(0.1)
            to_show, num = next(iterable_a)
        except ValueError:
            to_show[num] = ' '
            time.sleep(0.1)
            to_show[num] = '_'