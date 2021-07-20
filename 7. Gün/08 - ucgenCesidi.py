"""Kullanıcıdan bir üçgenin kenarları için 3 adet kenar uzunluğu isteyin. Girilen kenar
uzunluklarına göre bu üçgenin eşkenar, ikizkenar veya çeşitkenar üçgen olma
durumunu kontrol edin.
"""


k1 = int(input("1. kenarı giriniz:"))
k2 = int(input("2. kenarı giriniz:"))
k3 = int(input("3. kenarı giriniz:"))

if k1 == k2 and k2 == k3:
    print("Eşkenar üçgen")
elif (k1 == k2 and k2 != k3) or (k1 == k3 and k3 != k2) or (k2 == k3 and k2 != k1):
    print("İkizkenar üçgen")
else:
    print("Çeşitkenar üçgen")