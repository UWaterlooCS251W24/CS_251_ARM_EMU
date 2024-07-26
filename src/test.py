#!/usr/bin/env python3

from cpu import CPU

code = [
'\t\tADDI X3, XZR, #5 \t @ this is a comment',
'     \t CBZ XZR, #4 \t\r\n; this is another comment',
'ADDI X1, XZR, #5 ;;;; commenting again',
'ADDI X2, XZR, #10',
'ADD X3, X1, X2',
'STUR X3, [XZR, #8]'
]

cpu1 = CPU('Test', code, '', '')

cpu1.set_print_mode(hex_mode=False)

cpu1.run()

print(cpu1)
