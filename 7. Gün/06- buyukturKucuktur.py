"""
Kullanıcıdan iki tam sayı değeri alın ve aralarında büyük olanı ekrana yazdırın.
"""

sayi1 = int(input("1.sayıyı giriniz:"))
sayi2 = int(input("2.sayıyı giriniz:"))

if sayi1 > sayi2:
    print("1.Sayı Büyüktür. Sayı:" + str(sayi1))
elif sayi2 > sayi1:
    print("2.Sayı Büyüktür. Sayı:" + str(sayi2))
else:
    print("İki Sayı Birbirine Eşittir.")