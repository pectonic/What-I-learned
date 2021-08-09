havadurumu = 'karli'

if (havadurumu == 'yagmurlu'):
    print('semsiye al')
elif(havadurumu == 'karli'):
    print('lan wtf ne kari amk yaz ayindayiz')
else:
    print('sikinti yok') 

yas = 30
if (yas > 20):
    print('girebilirsin')
else:
    print('giremezsin') 

harfler =['a','b','c']
yoklama = 'd'

if yoklama in harfler:
    print('buradaaaa!')
else:
    print('yok amk ama eklerim :)')
    harfler.append('d')
    print('iste ekledim emmioglu {}:'.format(harfler))


if (yoklama in harfler) and (yoklama == harfler[3]):
    print('listede ve son elemean')
elif (yoklama in harfler):
    print('sadece listede')


