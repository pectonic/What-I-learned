def square(x):
    return x * x

print(square(square(2)))

# imput olmadan da func olur

def weird():
    return 22

print(weird())


# fonksiyonlar 'return' komutunu gordukten sonra asagidaki kodlara bakmaz

def square2(x):
    res = x*x
    return res
    print('LAAAA BENI ALMADIN LAN BENI ALMADIN ANASINI S')

print(square2(5))

def square2(x):
    res = x*x
    print('LAAAA BENI ALMADIN LAN BENI ALMADIN ANASINI S')

    return res

print(square2(5))
