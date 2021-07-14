#BAHŞİŞ HESAPLAYICI
print("--------Bahşiş Hesaplayıcıya Hoş Geldiniz--------------")
toplamUcret = float(input("Toplam fatura ne kadar tuttu? $"))
yuzde = input("Yüzde kaç bahşiş vermek istersiniz? %10,%12 veya %15 seçiniz.\n")
yuzdeTipi = int(yuzde)/100
kisiSayisi = int(input("Faturayı kaç kişi bölüşeceksiniz?\n"))
yeniToplam = float(toplamUcret) *yuzdeTipi
odeme = yeniToplam + toplamUcret
kisi = odeme/kisiSayisi
sonOdeme = round(kisi,2)
print("Kişi başı ödenecek tutar:${}".format(sonOdeme))