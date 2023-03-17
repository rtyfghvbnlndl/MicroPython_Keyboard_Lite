
def piano(buzz, keyboard, display, np):
    from time import sleep
    from random import randint

    index = (None,262,294,330,349,392,440,494,None,None,None,523,587,659,698,784,880,988,None,None,None,1046,1175,1318,1397,1568,1760,1976,)
    #tans = (-5,-4,-3,None,None,4,3,2,None,None,7,6,None,1,5,)
    tans = (5,6,7,None,None,1,2,3,4,None,-5,-4,-3)
    volume = (1,5,10,20,100,200,512)
    octave = 0
    duty = 1
    bpm=180

    display.fill(0)
    display.text('HAPPY', 0, 0)
    display.text('BIRTHDAY', 0, 8)
    display.show()

    for i in range(15):
        np[i]=(0,0,0)
    for i in (4,8,12):
        np[i]=(38,23,125)#八度变紫
    np[9]=(255,0,0)#退出变红
    np[3]=(0,255,0)#音量变绿
    np.write()

    def happy_birthday():
        a = (4,0.1,False,0,0.5,True,0,0.5,False,1,1,False,0,1,False,13,1,False,2,2,False,0,0.5,True,0,0.5,False,1,1,False,0,1,False,7,1,False,13,2,False,0,0.5,True,0,0.5,False,14,1,False,6,1,False,13,1,False,2,1,False,1,1,False,5,0.75,True,5,0.25,False,6,1,False,13,1,False,7,1,False,13,2,False)
        iteractor = iter(a)
        while True:
            try:
                yield next(iteractor)
            except StopIteration:
                iteractor = iter(a)
    
    a_generator = happy_birthday()
    print(a_generator)
    while True:
        print(a_generator)
        freq, num = 0, 0
        code = keyboard.scan_code()
        code.append(next(a_generator))
            
        if 4 in code:
            octave = 0
        elif 9 in code:
            octave =10
        elif 14 in code:
            octave = 20
        elif 13 in code:
            try:
                duty = volume[volume.index(duty)+1]
            except (IndexError, ValueError):
                duty = 1
        if 3 in code:
            while 3 in keyboard.scan_code():
                pass
            buzz.duty(0)
            display.fill(0)
            break
        
        for keys in (0,1,2,5,6,7,10,11,13,14,):
            if keys in code:
                np[keys]=(randint(0,255), randint(0,255), randint(0,255))
                try:
                    musical_note = tans[keys] + octave 
                    freq += index[musical_note]
                    num += 1
                except (TypeError, IndexError, ValueError):
                    pass
            else:
                np[keys] = (0, 0, 0)
        np.write()
        
        if num:
            freq = int(freq/num)
            #print(duty,freq)
            buzz.duty(duty)
            buzz.freq(freq)
        else:
            #print('mute')
            buzz.duty(0)

        sleep(next(a_generator)*60/bpm)
        if next(a_generator):
            buzz.duty(0)
            
        display.fill_rect(0, 16, 127, 23, 0)
        display.text('freq:' + str(freq), 0, 16)
        display.show()

        

        
   





