#!/usr/bin/env python3

from cpu import CPU

f = open('code/tabEx1.txt', 'r')
code = []
for line in f:
    code.append(line.strip())
f.close()

reg_config = '''

'''

cpu1 = CPU('Test', code, reg_config, '', True, True)

cpu1.set_print_mode(hex_mode=False)

cpu1.run()

print(cpu1)
