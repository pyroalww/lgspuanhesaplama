# Users/cagan/Documents/lgs puan hesaplama.py
import time
import os
import math
from tkinter import messagebox
from tkinter import simpledialog
import random
import datetime
from colorama import Fore


HEDEFMODU = simpledialog.askstring("Hedef Modu", "Hedef modu açılsın mı? Evet= 1 Hayır= 0")
if HEDEFMODU != "0" and HEDEFMODU != "1":
    print("Hatalı veri girdiniz!")
    exit()
HEDEFMODU = int(HEDEFMODU)
formul = """
LGS Puanı = (TürkçeNet * 4.348) + 
(T.C. İnk. TarihiNet * 1.666) + 
(Din KültürüNet * 1.899) + 
(Yabancı DilNet * 1.5075) + 
(MatematikNet * 4.2538) + 
(Fen BilimleriNet * 4.1230) + 
194.752082

"""

print("LGS Puanı hesaplama uygulamasına hoş geldiniz!")

turkceDogru = simpledialog.askstring("Türkçe", "Türkçe Doğru sayınızı giriniz: ")
turkceYanlis = simpledialog.askstring("Türkçe", "Türkçe Yanlış sayınızı giriniz: ")
turkceDogru = float(turkceDogru)
turkceYanlis = float(turkceYanlis)
turkceNet = turkceDogru - turkceYanlis / 3
if turkceNet > 20:
    messagebox.showerror("Hata", "Türkçe puanınız 20'den fazla olamaz!")
    exit()
tarihDogru = simpledialog.askstring("Tarih","T.C. İnk. Tarihi Doğru sayınızı giriniz: ")
tarihYanlis = simpledialog.askstring("Tarih","T.C. İnk. Tarihi Yanlış sayınızı giriniz: ")
tarihDogru = float(tarihDogru)
tarihYanlis = float(tarihYanlis)
tarihNet = tarihDogru - tarihYanlis / 3
if tarihNet > 10:
    messagebox.showerror("Hata","T.C. İnk. Tarihi puanınız 10'dan fazla olamaz!")
    exit()
dinKulturuDogru = simpledialog.askstring("Din","Din Kültürü Doğru sayınızı giriniz: ")
dinKulturuYanlis = simpledialog.askstring("Din","Din Kültürü Yanlış sayınızı giriniz: ")
dinKulturuDogru = float(dinKulturuDogru)
dinKulturuYanlis = float(dinKulturuYanlis)
dinKulturuNet = dinKulturuDogru - dinKulturuYanlis / 3
if dinKulturuNet > 10:
    messagebox.showerror("Hata","Din Kültürü puanınız 10'dan fazla olamaz!")
    exit()
yabanciDilDogru = simpledialog.askstring("İngilizce","Yabancı Dil Doğru sayınızı giriniz: ")
yabanciDilYanlis = simpledialog.askstring("İngilizce","Yabancı Dil Yanlış sayınızı giriniz: ")
yabanciDilDogru = float(yabanciDilDogru)
yabanciDilYanlis = float(yabanciDilYanlis)
yabanciDilNet = yabanciDilDogru - yabanciDilYanlis / 3
if yabanciDilNet > 10:
    messagebox.showerror("Hata","Yabancı Dil puanınız 10'dan fazla olamaz!")
    exit()
matematikDogru = simpledialog.askstring("Matematik","Matematik Doğru sayınızı giriniz: ")
matematikYanlis = simpledialog.askstring("Matematik","Matematik Yanlış sayınızı giriniz: ")
matematikDogru = float(matematikDogru)
matematikYanlis = float(matematikYanlis)
matematikNet = matematikDogru - matematikYanlis / 3
if matematikNet > 20:
    messagebox.showerror("Hata","Matematik puanınız 20'den fazla olamaz!")
    exit()
fenbilimleriDogru = simpledialog.askstring("Fen","Fen Bilimleri Doğru sayınızı giriniz: ")
fenbilimleriYanlis = simpledialog.askstring("Fen","Fen Bilimleri Yanlış sayınızı giriniz: ")
fenbilimleriDogru = float(fenbilimleriDogru)
fenbilimleriYanlis = float(fenbilimleriYanlis)
fenbilimleriNet = fenbilimleriDogru - fenbilimleriYanlis / 3
if fenbilimleriNet > 20:
    messagebox.showerror("Hata","Fen Bilimleri puanınız 20'den fazla olamaz!")
    exit()

# Hesaplama işlemi
yanlissizPuan = (turkceDogru * 4.348) + (tarihDogru * 1.666) + (dinKulturuDogru * 1.899) + (yabanciDilDogru * 1.5075) + (matematikDogru * 4.2538) + (fenbilimleriDogru * 4.1230) + 194.752082
puan = (turkceNet * 4.348) + (tarihNet * 1.666) + (dinKulturuNet * 1.899) + (yabanciDilNet * 1.5075) + (matematikNet * 4.2538) + (fenbilimleriNet * 4.1230) + 194.752082 
puanFarki = puan - yanlissizPuan
if puan >= 499:
    puan = 500
if puan == 500:
    durum = "Tebrikler. Tam puan aldınız."
elif puan >= 470:
    durum = "Puanınız gayet iyi. Çalışmaya devam ederseniz 500 alabilirsiniz."
elif puan >= 440:
    durum = "Puanınız iyi. Çalışmaya devam ederseniz daha iyi puanlar alabilirsiniz."
elif puan >= 400:
    durum = "Puanınız orta derecede. Çalışmaya devam ederseniz daha iyi puanlar alabilirsiniz."
elif puan < 400:
    durum = "Puanınız yetersiz. Çalışmaya devam ederseniz daha iyi puanlar alabilirsiniz."
if HEDEFMODU == 1:
    tahmin = simpledialog.askinteger("Tahmin Modu","Puanınızı tahmin ediniz: ")
    sonuc = puan - tahmin
    if sonuc == 0:
        fark = "Fark yok!"
    elif sonuc > 0:
        fark = "Kendinize güvenin."
    elif sonuc < 0:
        fark = "Puanınız beklediğinizden bir miktar aşağıda."
    print(f"Tahmin farkınız: " + str(sonuc))
os.system("clear")
print("LGS Puanınız: ", puan)
datetime = datetime.datetime.now()
datetime = str(datetime)
SINAVOZETI = """Sınav özetiniz:
Tarih: {}

Sınav Puanınız: {}
Tüm yanlışlarınızı boş bıraksaydınız puanınız: {}
Tüm yanlışlarınızı boş bıraksaydınız alacağınız + puan: {}
Durumunuz: {}
Tahmininiz: {}
Farkınız: {}
====================================
Türkçe Netiniz: {}
T.C. İnk. Tarihi Netiniz: {}
Din Kulüpleri Netiniz: {}
Yabancı Dil Netiniz: {}
Matematik Netiniz: {}
Fen Bilimleri Netiniz: {}
====================================
""".format(datetime, puan, yanlissizPuan, puanFarki, durum, tahmin, fark, turkceNet, tarihNet, dinKulturuNet, yabanciDilNet, matematikNet, fenbilimleriNet)
print(SINAVOZETI)
messagebox.showinfo("Sonucunuz", SINAVOZETI)


with open('LGS Puan Hesaplama.txt', 'w') as f:
    f.write(SINAVOZETI)
import tkinter as tk


def secim_yap(ana_pencere):
    secenekler = ['Yeniden dene', 'Çıkış yap']

    def secildi(secim):
        if secim == 'Yeniden dene':
            ana_pencere.destroy()
            os.system("python3 lgs puan hesaplama.py")
        elif secim == 'Çıkış yap':
            ana_pencere.destroy()
            exit()
        ana_pencere.destroy()

    for secenek in secenekler:
        button = tk.Button(ana_pencere, text=secenek, command=lambda secenek=secenek: secildi(secenek))
        button.pack()

ana_pencere = tk.Tk()
secim_yap(ana_pencere)
ana_pencere.mainloop()

