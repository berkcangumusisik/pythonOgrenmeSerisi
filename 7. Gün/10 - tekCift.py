"""
Kullanıcıdan bir sayı alınız. Sayı 0'dan büyükse pozitif , 0'dan küçükse negatif 
sıfıra eşitse sıfır yazdırınız.
"""

sayi = int(input("Bir sayı giriniz:"))

if sayi > 0:
    print("Pozitif tam sayıdır.")
    
elif sayi < 0:
    print("Negatif tam sayıdır.")
else:
    print("Sayı sıfırdır.")