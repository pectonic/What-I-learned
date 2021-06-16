'''amac: sehir ve tarih secildikten sonra ona gore islenmis suclari guide gostermek'''

from tkinter import *
from tkinter.font import BOLD
from tkcalendar import DateEntry 
from tkinter import messagebox
import requests 
from typing import Counter



class suc_analiz():

    def __init__(self,bolge,tarih,suc_turu = "all-crime"):
        self.bolge = bolge
        self.tarih = tarih
        self.suc_turu = suc_turu
        self.suclar = self.suclari_bul()


    def suclari_bul(self): #suclari almak icin func yazalim
        suc_URL = 'https://data.police.uk/api/crimes-no-location' #APIyi cekiyoruz

        payload = { #keyleri yaziyoruz
            'category' : self.suc_turu,
            'force' : self.bolge,
            'date' : self.tarih
        }
        response = requests.get(suc_URL, params=payload)#geri bildrimi aliyoruz

        if response.status_code == 200: #basarili cekip cekmedigini soruyoruz
            return response.json() #basariliysa aktariyoruz
        else:
            return None #basarisiz olursa none gondersin ki hata vermesin
    
    

    def suclari_say(self): #hangi suc kac kere islenmis acep

        suclar_listesi = [] #suclari listlemek icin bos bir liste

        if self.suclar is not None: #none degilde insin ki yine patlamayalim
            for suc in self.suclar: #suclar icinde gez ve
                suclar_listesi.append(suc['category']) #suclar_listesi'ne yolla
            
            return Counter(suclar_listesi)#counter hangi sonucun kac kere dondugunu bize gosteriyor 

'''ALT TARAF GUI VS'''

master = Tk()

canvas = Canvas(master, height=450 , width=750)
'''
pack
place
grid
'''

canvas.pack()

frame_ust = Frame(canvas, bg='#add8e6')
frame_ust.place(relx= 0.05, rely=0.05, relheight=0.1, relwidth=0.9)



frame_alt_sag = Frame(canvas, bg='#add8e6')
frame_alt_sag.place(relx= 0.05, rely=0.18, relheight=0.7, relwidth=0.9)

hatirlatma_tipi_etiket = Label(frame_ust, bg='#add8e6', text='Sehir',font='Verdana 18 bold' )
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set('\t')

def bolgeleri_bul():
        forces_URL = 'https://data.police.uk/api/forces'

        response = requests.get(forces_URL)

        bolgeler = response.json()

        bolgeler_liste = []
        for bolge in bolgeler:
            bolgeler_liste.append(bolge.get('id'))

        return bolgeler_liste


hatirlatma_tipi_acilir_menu = OptionMenu(
    frame_ust,
    hatirlatma_tipi_opsiyon,
    *bolgeleri_bul()
)
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_tarih_secici = DateEntry(frame_ust, width= 12, background = 'orange', foreground='black', borderwidth = 1, locale="de_DE")
hatirlatma_tipi_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tipi_tarih_secici.pack(padx=10, pady=10, side=RIGHT)


hatirlatma_tipi_etiket2 = Label(frame_ust, bg='#add8e6', text='Tarih:',font='Verdana 18 bold' )
hatirlatma_tipi_etiket2.pack(padx=10, pady=10, side=RIGHT) 


var = IntVar()

varc3 = IntVar()


def analiz():
    if hatirlatma_tipi_opsiyon.get() is not None:
        bolge = hatirlatma_tipi_opsiyon.get()
        tarih = str(hatirlatma_tipi_tarih_secici.get_date())
        tarih_asil = '{}-{}'.format(tarih[6:10],tarih[0:2])
        denemee = suc_analiz('{}'.format(bolge), '{}'.format(tarih_asil))
        for suclar in range(len(denemee.suclari_say())):
            mylist.insert(suclar, "Python")
        
        
        


    


        


analiz_butonu = Button(frame_alt_sag, text="Analiz et", command=analiz)
analiz_butonu.pack(anchor=NE, pady=10, padx=10) 

Label(frame_alt_sag, bg='#add8e6', text='SONUCLAR',font='Verdana 12 bold').pack(padx=10, pady=10, anchor=NW)


suclar_sehirler = Scrollbar(frame_alt_sag)
suclar_sehirler.pack(side = RIGHT, fill = Y)
mylist = Listbox(frame_alt_sag, yscrollcommand = suclar_sehirler.set, height=15, width=80 )


mylist.pack( side = RIGHT, fill=BOTH )
suclar_sehirler.config( command = mylist.yview )



'''

def analiz():
    
    islem_sonrasi_text = ""
    try:
        if var.get():
            if var.get() == 1:
                islem_sonrasi_text += "Sisteme kaydedilmistir!"

                tip = hatirlatma_tipi_opsiyon.get()
                tarih = hatirlatma_tipi_tarih_secici.get_date()
                mesaj = txbox.get("1.0","end")

                with open("hatirlatmalar.txt", "w") as dosya:
                    dosya.write(
                        "{} karegorisinde, {} tarihine ve {} notuyla hatirlatma".format(tip,tarih,mesaj))
                    dosya.close()

            elif var.get() == 2:
                islem_sonrasi_text += "E-posta yolu basarili!"
            
            messagebox.showinfo("Basarili islem", islem_sonrasi_text)

        else:
            islem_sonrasi_text += "YAV KARDESIM ISLEM SECSENE!"
            messagebox.showwarning("YAZILIM OGRENSEYDIN AMMMMMCIK",islem_sonrasi_text)
    except:
        islem_sonrasi_text += "HATA HATA HATA"
        messagebox.showerror("YAZILIM OGRENSEYDIN AMMMMMCIK",islem_sonrasi_text)
    finally:
        master.destroy()

    return'''






master.mainloop() 