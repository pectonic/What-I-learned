import re

arama_cumlesi = 'asd sdasd fjasdnf ja fojsavna ao   asdoke2nrpnmfp a a akewnmrkknwea kenfkwnf'

arama_keyi = 'asd'

'''
arama yapiyor cumlenin icinde
'''
eslesme = re.search(arama_keyi, arama_cumlesi)



#################################################################################
# ####### Ifade ########## Aciklama ######## Örnek ########### Patern ########### 
# ####### --------------------------------------------------------------- ####### 
# ####### \d ######### rakam ####### base42    #########   base\d\d     ######### 
# ####### \w ######## karakter ##### R2-D2     #########    \w\w\w\w\w   ######## 
# ####### \s ######## bosluk ###### Ping Pong   ######## Ping\sPong      ######## 
# ####### \D ####### rakam degil ##### base    ######### \D\D\D\D       ######### 
# ####### \W ##### karakter degil ### R2D2     ######### \W\W\W\       ########## 
# ####### \S ##### bosluk degil ##### PingPong ###     \S\S\S\S\S\S\S\S   ####### 
# ####### --------------------------------------------------------------- ####### 
# ###############################################################################

######## Ifade ####### Aciklama ######## Örnek ############# Patern ############## 
# ####### ---------------------------------------------------------------- #######
# ####### {5}   ######## adet ####### aaaaa     #########       \w{5}   ########## 
# ####### {3,4} ####### veya ####### abc        #########       \w{3,4   ######### 
# ####### {2,}  ######## en az ##### 198721321  ########       \d{2,}    ######### 
# ####### *     ### 0 ya da fazla ####### x     ##########       \w*      ######## 
# ####### +     ### 1 ya da fazla ###### Ahmet1 #######         \w+\     ######### 
# ####### ?     ##### ya 1 ya hic ####### Mura  #########      Murat?       ###### 
# ####### --------------------------------------------------------------- ######## 
# ################################################################################

######## Ifade ####### Aciklama ######## Örnek ############# Patern ############ 
# ####### ---------------------------------------------------------------- ####### 
# ####### | ######## veya       #######    slm      #########  selam|slm  ######## 
# ####### ^ ####### baslar      #######   Ahmet    ##########  ^\w+       ######## 
# ####### $   ########  biter     #####   base42     ########  \d$        ######## 
# ####### . ###### herhangi       #####   abcdef     ########   .*        ######## 
# ####### \ ######## esc          #####   (not)      ######   $\w{3}$     ######## 
# ####### --------------------------------------------------------------- ######## 
# ################################################################################


#print(dir(eslesme))#bu zaten kendisine ait komutlari donduruyor
#print(eslesme.start())#baslangic span noktasini gosteriyor 
#print(eslesme.end()) # kanka bu da son span noktasi 

for paterns in re.finditer(arama_keyi, arama_cumlesi): #normalde ilk spani verirdi bize ama finditer ile span ve group kullanimini destekledi
        #print(paterns.span(), paterns.group())
        pass

cumle = 'selam benim telefon numaram: 0538-058-6969'
cumle_arama = r'\d\d\d\d-\d\d\d-\d\d\d\d' 
cumle_arama = r'\d{3,4}-\d{3}-\d{4}'# ustte arayabildigin gibi bunun gibi de arayabilirsen

eslesme2 = re.search(cumle_arama, cumle)
#print(eslesme2.span(), eslesme2.group()) 

cumle2 = 'en sevdigim ulke Japonya'
cumle2_arama = r'\s\w{5,}'#burada \s ile bosluk \w{5,} ile 5 ve daha fazla karakterli olanlari aldim ve tabii ki JAPONYA karakterli :))))))))))))))))))))))))))
cumle2_eslesme = re.search(cumle2_arama, cumle2)
for eslesme in re.finditer(cumle2_arama, cumle2):
        #print(eslesme.span(), eslesme.group())
        pass


cumle3 = 'her allahin gunu en az 5000 metre yani 5 km yurumeye cikiyorum'
cumle3_arama= r'\d?'#bu her buldugu sayiyi bize verir

for eslesme in re.finditer(cumle3_arama, cumle3):
        #print(eslesme.span(), eslesme.group()) #burada hepsi doner ama sadece sayilari gruplar cunku onu soyledik amk ne verecek baska
        pass

cumle3_arama = r'\d{2,}?'#deneyim bakayim olacak mi, ikili ikili aldi amk :D neyse

for eslesme in re.finditer(cumle3_arama, cumle3):
        #print(eslesme.span(), eslesme.group())
        pass

cumle3_arama = r'\d*' # bu da 0 yada daha fazla, LAN HEPSINI MI ALACAK AMK, aynen yine hepsini tariyor ama \d oldugundan sadece sayilari aliyor

for eslesme in re.finditer(cumle3_arama, cumle3):
        #print(eslesme.span(), eslesme.group())
        pass

cumle3_arama= r'\d+' #ADAM YA GELDI ADAM, BU 1 VEYA DAHA FAZLASINI ALIYOR BU YUZDEN 0LAR YOK BABBA

for eslesme in re.finditer(cumle3_arama, cumle3):
        #print(eslesme.span(), eslesme.group())
        pass

op_turkcell= r'\d*53\d+'
op_avea= r'\d*50\d+'
op_vodofone= r'\d*54\d+'

def gsm_op_bul():
        telefon_no= input('tel no vre: ')
        if re.search(op_turkcell, telefon_no):
                return 'sen turkcell kullaniyon ve numaran: {}'.format(telefon_no)
        elif re.search(op_avea, telefon_no):
                return 'sen avea kekw aslinda komik bir sey yok ben malim ;s ve numaran: {}'.format(telefon_no)
        elif re.search(op_vodofone, telefon_no):
                return 'vodofone kekw degil guzle ve numaran: {}'.format(telefon_no)
        else:
                return 'baska'

#print(gsm_op_bul())

def mesaj_hissi_bul(cumle):
        hisler= []
        pozitif_patern = r"(merhaba|selam|ask|sevgi|dost|kardes|:\)+)"
        negatif_patern = r"(lan|aptal|abv|yeter|birak)"
    
        heyecanli_patern = r"!|[!|?]{2,}$"
        sakin_patern = r"^[Tabi+|Hayhay]"
    
        emin_patern = r"[K|k]esin|[T|t]abi|[E|e]lbet"
        kararsiz_patern = r"[B|b]elki|[S|s]anirim"

        if re.search(pozitif_patern, cumle):
                hisler.append('pozitif')
        if re.search(negatif_patern, cumle):
                hisler.append('negatif')
        if re.search(heyecanli_patern, cumle):
                hisler.append('heyecanli')
        if re.search(sakin_patern, cumle):
                hisler.append('sakin')
        if re.search(emin_patern, cumle):
                hisler.append('emin')
        if re.search(kararsiz_patern, cumle):
                hisler.append('karasiz')

        return hisler
                

cumle1 = "Naber abi? :)             "
cumle2 = "Tabiii ki buyrun          "
cumle3 = "Sacmalamayi birak artik!  "
cumle4 = "Belki yarindan da yakin..."
cumle5 = "Elbet birgün bulusacagiz  "
cumleler = [cumle1, cumle2, cumle3, cumle4, cumle5]
for cumle in cumleler :
    print(cumle, '\t', mesaj_hissi_bul(cumle))