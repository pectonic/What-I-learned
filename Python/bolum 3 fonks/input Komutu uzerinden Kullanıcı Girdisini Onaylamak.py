
"""
def sayi_control():
    deger = input('deger gir baqim: ')
    
    while not deger.isdigit(): #isdigit sayi mi degolmi onu check ediyor
        print(' sayi girmelisin yoksa cikis yok')
        deger = input('deger gir: ')

    else:
        print(' bu sayi karsim')

        

print(sayi_control())
"""
def mail_check():
    deger = input('mail gir: ')

    while not (('@' in deger) and ( '.' in deger)):
        print(' lan caqal duzgun mail gir! ')
        deger = input('gir LA: ')
    else: 
        print('guzel guzel yeriz')

print(mail_check())