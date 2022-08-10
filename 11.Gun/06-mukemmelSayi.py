""" 
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).
"""

def mukemmel_mi(sayı):
    toplam = 0
    for i in range(1,sayı):
        if (sayı % i == 0):
            toplam += i
    return toplam == sayı

for i in range(1,1000):
    if (mukemmel_mi(i)):
        print("Mükemmel Sayı:",i)