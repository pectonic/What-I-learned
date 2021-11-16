# Python'da fonksiyonlar first class function olarak değerlendirilir. Bunun anlamı fonksiyonların diğer veri tipleri gibi manipüle edilebilir ve başka fonksiyonlara argüman olarak verilebilir.

# Bir fonksiyonu bir değişkene atayabiliriz.

def square(x):
    return x*x

print(square(5))

a = square

print(a(4))


# Bir fonksiyonu başka bir fonksiyona argüman olarak verebiliriz.

def f2(x, f):
    return f(x) + 4

f2(3,square)

def f3(x):
    return x**5

f2(2, f3)
