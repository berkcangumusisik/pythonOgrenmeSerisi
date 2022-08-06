
""" 
Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışın.

Örnek olarak, Bir sayı eğer 4 basamaklı ise ve oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı( 3 basamaklı sayılar için 3.kuvveti ) o sayıya eşitse bu sayıya "Armstrong" sayısı denir.

Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4
"""
sayi = input("Sayı:")
basamakSayisi = len(sayi)
sayi = int(sayi)
basamak = 0
toplam = 0

geciciSayi = sayi

while (geciciSayi> 0):
    
    basamak = geciciSayi % 10
    
    toplam += basamak ** basamakSayisi
    
    geciciSayi //= 10
    

if toplam == sayi:
    print("{} armstrong bir sayıdır.".format(sayi))
else:
    print("{} armstrong bir sayı değildir.".format(sayi))