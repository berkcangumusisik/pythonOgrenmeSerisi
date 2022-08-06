""" 
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. 

Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
sayi = int(input("Sayı:"))
i = 1
toplam = 0
while i < sayi:
    if sayi % i == 0:
        toplam += i
    i += 1
    
if toplam == sayi:
    print("{} mükemmel bir sayıdır.".format(sayi))
else:
    print("{} mükemmel bir sayı değildir.".format(sayi))