""" 
Kullanıcının girdiği sayının asal olup-olmadığını kontrol eden bir program yazın.
"""

sayi = int(input("Bir sayı giriniz : "))
sayac = 0
for i in range(2, sayi):
    if(sayi % i == 0):
        sayac =  1
        break
    
if(sayac == 1):
    print("Asal sayı değildir.")
else:
    print("Asal sayıdır.")