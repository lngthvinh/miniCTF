def up(x):
    x = [f"{ord(x[i]) << 1:08b}" for i in range(len(x))]
    return ''.join(x)

def down(x):
    x = ''.join(['1' if x[i] == '0' else '0' for i in range(len(x))])
    return x

def right(x,d):
    x = x[d:] + x[0:d]
    return x

def left(x,d):
    x = right(x,len(x)-d) 
    return x[::-1] 
    
def encode(plain):
    d = 32
    x = up(plain)
    x = right(x,d)
    x = down(x)
    x = left(x,32)
    return x

def rUp(x):
    outs = [chr(int(x[i:i+8],2) >> 1) for i in range(0, len(x), 8)] 
    return ''.join(outs)

def rRight(x,d):
    x = x[len(x) - d:] + x[0:len(x) - d]
    return x

def decode(plain):
    d = 32

    x = left(plain,d)
    x = down(x)
    x = rRight(x,d)
    s = rUp(x)
    return s

def main():
    flag = "ISPCLUB{}"
    encoded = encode(flag)
    print(encoded)
    print("What does this mean?")

    if (decode(encoded) == flag):
        print('Check? True')
    else:
        print('Check? False')
        return
    
    encoded = "10100000101100011100010010111101100110001101100010101100110010001001100111011000100000101111100111101000100000101001100110100100111110011001110010000010111001001110010010011001100010101001000011011110101010101110011010011110111110101001101010110110"
    decoded = decode(encoded)
    print(decoded)

if __name__ == "__main__":
  main()

#> ISPCLUB{W3ll_c0m3_t0_r3vers!n9}
