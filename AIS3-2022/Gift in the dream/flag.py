# AIS3{5T3g4n0gR4pHy_c4N_b3_fUn_s0m37iMe}
# https://www.sqlsec.com/2018/01/ctfimg.html
import sys

for s in sys.stdin:
    a = s.split(' ')
    print(chr(int("".join(a[1:2]))),end='')