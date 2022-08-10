""" 
Kullanıcıdan 2 basamaklı bir sayı alın ve bu sayının okunuşunu bulan bir fonksiyon yazın.

Örnek: 97 ---------> Doksan Yedi
"""
birler =  ["","Bir","İki","Üç","Dört","Beş","Alti","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Krık","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):
    birinci = sayi % 10
    ikinci = sayi // 10
    
    return onlar[ikinci] + " " + birler[birinci]

    
sayi =  int(input("Sayı:"))

print(okunus(sayi))