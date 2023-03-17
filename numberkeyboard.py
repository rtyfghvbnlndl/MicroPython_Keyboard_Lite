def board(keyboard,np,output,display):
    from random import randint
    from time import sleep

    #index = ('1','2','3','0','(','.','6','5',"+",None,'9','8','-','4','7')
    index = ('7','8','9',None,'+','4','5','6',".",'(','1','3','4','0','-')

    display.fill(0)
    display.text('number', 0, 0)
    display.text('keyboard', 0, 8)
    display.show()

    for i in range(15):
        np[i]=(0,0,0)
    np[3]=(255,0,0)#退出变红
    np.write()
    while True:
        try:
            code = keyboard.scan_code()[0]
            if code != 9:
                np[code]=(randint(0,255), randint(0,255), randint(0,255))
                np.write()
                while code in keyboard.scan_code():
                    pass
                try:output.write(index[code].encode('ascii'))
                except:
                    print('erro')
            else:
                while 3 in keyboard.scan_code():
                    pass
                display.fill(0)
                break
            np[code]=(0,0,0)
            np.write()
        except IndexError:
            pass
        sleep(0.05)
        
        