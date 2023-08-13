from tkinter import*

window = Tk()
window.title("BMI")
window.minsize(width=300, height=300)

my_kilo_label = Label(text="Kilonuzu Girin(kg)")
my_kilo_label.pack()

my_kilo_entry = Entry()
my_kilo_entry.pack()

my_boy_label = Label(text="Boyunuzu Girin(cm)")
my_boy_label.pack()

my_boy_entry = Entry()
my_boy_entry.pack()

my_massage_label = Label(text=" ")
my_massage_label.pack()

def Hesapla():
    boy = my_boy_entry.get()
    kilo = my_kilo_entry.get()


    if boy == "" or kilo == "":
        my_massage_label.config(text="boy ve kilo giriniz")
    else:
        try:
            ort = float(kilo) / (float(boy) / 100) ** 2
            if ort < 18.49:
                my_massage_label.config(text="ideal kilonun altındasınız")
            elif ort > 30:
                my_massage_label.config(text="ideal kilonun çok üzerindesiniz")
            elif ort > 18.49 and ort < 24.99:
                my_massage_label.config(text="ideal kilodasınız")
            elif ort < 29.99 and ort > 25:
                my_massage_label.config(text="ideal kilonun üzerindesiniz")
        except:
            my_massage_label.config(text="boy ve kilo giriniz")




my_button = Button(text="Hesapla",command=Hesapla)
my_button.pack()

window.mainloop()



