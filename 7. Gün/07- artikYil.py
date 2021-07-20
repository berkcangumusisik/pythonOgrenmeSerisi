"""Bir yılın artık yıl olup olmadığını kontrol etmek için bir program yazın. 
Artık yıl kuralı:
a) Eğer yılın son iki basamağı (00) ile bitmiyorsa yalnızca 4'e tam bölünmesi
gerekir.
b) Eğer yılın son iki basamağı (00) ile bitiyorsa hem4'e hem de 400' e tam
bölünmesi gerekir.Örneğin 1905 sayısının son iki basamağı 00 olmadığı için
yalnızca 4 sayısına tam bölünmesi kontrol edilmelidir. Ancak 1900 sayısının
son iki basamağı 00 ile bittiği için hem 4'e hem de 400'e tam bölünmesi
kontrol edilmelidir.
"""

yil = int(input("Bir yıl giriniz:"))

if yil % 4  == 0:
    if yil % 100  == 0:
        if yil % 400  == 0:
            print("Artık yıl")
        else:
            print("Artık yıl değil")
    else:
        print("Artık yıl")
else:
    print("Artık yıl değil")