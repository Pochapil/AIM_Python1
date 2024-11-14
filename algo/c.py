def euclid(a, b):
    if b == 0:
        print(a, '&', b, '&', '&', '-', '&', '&', r'\\')
        return
    print(a, '&', b, '&', '&', a // b, '&', '&', r'\\')
    euclid(b, a % b)


a = 68
b = 561
euclid(a, b)
