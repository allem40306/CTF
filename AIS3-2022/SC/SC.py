str1 = ""
str2 = ""
str3 = ""
tb = {}

with open("cipher.py", "r",encoding="utf-8") as f:
    for s in f.readlines():
        str1 += s

with open("cipher.py.enc", "r",encoding="utf-8") as f:
    for s in f.readlines():
        str2 += s

with open("flag.txt.enc", "r",encoding="utf-8") as f:
    for s in f.readlines():
        str3 += s

for i in range(len(str1)):
    tb[str2[i]] = str1[i]

for ch in str3:
    print(tb[ch],end='')