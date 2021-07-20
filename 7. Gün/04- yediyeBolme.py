"""Bir sayının 7'ye bölünebilir olup olmadığını kontrol etmek 
için bir program yazın.
"""

print("***********7'ye Bölme Uygulamasına Hoş Geldiniz***********")
sayi = int(input("Bir sayı giriniz: "))

if sayi % 7 == 0:
    print("Sayı 7'ye tam bölünüyor")
else:
    print("Sayı 7'ye tam bölünmüyor")
