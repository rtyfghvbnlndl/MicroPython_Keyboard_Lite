import py_keybord

keybord = py_keybord.keybord((0,1,6,7),(9,8,4,5))

print('keybord_size:%ix%i' % (keybord.out_length,keybord.in_length))

L0 = keybord.scan_single(0)
print(L0)

all = keybord.scan()
print(all)

code = keybord.scan_code()
print(code)