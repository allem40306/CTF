val = [45,71,155,115,131,227,35]

def f(c1):
    if c1 >= ord('0') and c1 <= ord('9'):
        return c1-ord('0')
    else:
        return c1-ord('a') + 10

def getArr():
    arr = []
    str = open("output.txt", "rb").read().strip()
    for i in range(0,len(str),2):
        arr.append(f(str[i]) * 16 + f(str[i+1]))
    return arr

# AIS3{not_every_bits_are_used_lol}
if __name__ == "__main__":
    arr = getArr()
    str = ""
    for i in range(len(arr)):
        if i < len(val):
            str += chr(arr[i] ^ val[i])
        else:
            str += chr(arr[i] ^ 163)
    print(str)