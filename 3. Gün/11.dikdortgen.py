"""
Dikdörtgenin iki kenar uzunluğunu kullanıcıya sorup, dikdörtgenin çevresini ve alanını hesaplayan bir program yazınız

İpucu: Kenar uzunluklarını input ile alabilirsiniz.

Örnek
>>>input: 
6 , 4

>>>output:
Çevre: 20
Alan: 24 
"""
kisa = input('Kısa Kenar : ')
uzun = input('Uzun Kenar : ')
alan = int(kisa) * int(uzun)
cevre = 2 * (int(kisa) + int(uzun))
print("Dikdörtgenin alanı : ",alan)
print("Dikdörtgenin çevresi :",cevre)