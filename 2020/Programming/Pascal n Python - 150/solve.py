arr = [265, 275, 272, 259, 268, 277, 258, 283, 211, 257, 275, 281, 255, 274, 209, 263, 264, 276, 223, 285]
flag = ""

for i in arr:
    flag += chr(i - 160)

print(flag)