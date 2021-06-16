from tkinter import *
from tkinter.font import BOLD
from tkcalendar import DateEntry 
from tkinter import messagebox


master = Tk()

canvas = Canvas(master, height=450 , width=750)
'''
pack
place
grid
'''

canvas.pack()

frame_ust = Frame(canvas, bg='#add8e6')
frame_ust.place(relx= 0.1, rely=0.1, relheight=0.1, relwidth=0.8)

frame_alt_sol = Frame(canvas, bg='#add8e6')
frame_alt_sol.place(relx= 0.1, rely=0.21, relheight=0.7, relwidth=0.23)

frame_alt_sag = Frame(canvas, bg='#add8e6')
frame_alt_sag.place(relx= 0.34, rely=0.21, relheight=0.7, relwidth=0.56)

hatirlatma_tipi_etiket = Label(frame_ust, bg='#add8e6', text='Hatirlatma Tipi',font='Verdana 18 bold' )
hatirlatma_tipi_etiket.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_opsiyon = StringVar(frame_ust)
hatirlatma_tipi_opsiyon.set('\t')

hatirlatma_tipi_acilir_menu = OptionMenu(
    frame_ust,
    hatirlatma_tipi_opsiyon,
    'dogum gunu',
    'alisveris',
    'odeme'
)
hatirlatma_tipi_acilir_menu.pack(padx=10, pady=10, side=LEFT)

hatirlatma_tipi_tarih_secici = DateEntry(frame_ust, width= 12, background = 'orange', foreground='black', borderwidth = 1, locale="de_DE")
hatirlatma_tipi_tarih_secici._top_cal.overrideredirect(False)
hatirlatma_tipi_tarih_secici.pack(padx=10, pady=10, side=RIGHT)


hatirlatma_tipi_etiket2 = Label(frame_ust, bg='#add8e6', text='Tarih:',font='Verdana 18 bold' )
hatirlatma_tipi_etiket2.pack(padx=10, pady=10, side=RIGHT) 

Label(frame_alt_sol, bg='#add8e6', text='Hatirlatma Yontemi:',font='Verdana 12 bold').pack(padx=10, pady=10, anchor=NW)

var = IntVar()

r1 = Radiobutton(frame_alt_sol, text='Sisteme kaydet', variable=var, value=1, font='Verdana 10', bg='#add8e6')
r1.pack(padx=15, pady=5, anchor=NW)

r2 = Radiobutton(frame_alt_sol, text='E-posta gonder', variable=var, value=2, font='Verdana 10', bg='#add8e6')
r2.pack(padx=15, pady=5, anchor=NW)

varc1 = IntVar()
c1 = Checkbutton(frame_alt_sol, text='1 hafta once gonder', variable=varc1, onvalue=1, offvalue=0, font='Verdana 8', bg='#add8e6')
c1.pack(padx=25, pady=2, anchor=NW)

varc2 = IntVar()
c2 = Checkbutton(frame_alt_sol, text='1 gun once gonder', variable=varc2, onvalue=1, offvalue=0, font='Verdana 8', bg='#add8e6')
c2.pack(padx=25, pady=2, anchor=NW)

varc3 = IntVar()
c3 = Checkbutton(frame_alt_sol, text='1 ay once gonder', variable=varc3, onvalue=1, offvalue=0, font='Verdana 8 ', bg='#add8e6')
c3.pack(padx=25, pady=2, anchor=NW)


Label(frame_alt_sag, bg='#add8e6', text='Hatirlatma Mesaji:',font='Verdana 12 bold').pack(padx=10, pady=10, anchor=NW)

def gonder():
    
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

    return


gonder_butonu = Button(frame_alt_sag, text="Gonder", command=gonder)
gonder_butonu.pack(anchor=NE, pady=10)

txbox = Text(frame_alt_sag, height=15, width=50)
txbox.tag_configure('style', foreground='#bfbfbf', font=('Verdana', 16, 'italic'))
txbox.pack()
karsilama_metni= 'Mesaj gir...'
txbox.insert(END,karsilama_metni, 'style')





master.mainloop() 