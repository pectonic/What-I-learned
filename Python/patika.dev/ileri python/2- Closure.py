# Bir fonksiyonun içinde tanımlanmış fonksiyonun, dışındaki fonksiyonun içinde tanımlanmış değişkenlere, dıştaki fonksiyon çağrılmış olsa da erişebilmesidir.

def outer(msg):
    msg = msg

    def inner():
        print(msg)

    return inner


deneme = outer("UYAN LAN")

print(deneme())  
