"""Tebrikler, Python Pizza'da bir işiniz var. İlk işiniz otomatik bir pizza sipariş programı oluşturmak.

Bir kullanıcının siparişine göre, son faturasını hesaplayın.

Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25
Pepperoni for Small Pizza: +$2
Pepperoni for Medium or Large Pizza: +$3
Extra cheese for any size pizza: + $1
Örnek Giriş
size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
Örnek Çıktı
Your final bill is: $28."""

print("*** Python Pizza'a Hoş Geldiniz ***")
boyut = input("Pizzanız hangi boy olsun? S, M veya L seçiniz:\n")
biber = input("Ekstra biber ister misiniz? E veya H\n")
peynir = input("Ekstra peynir ister misiniz? E veya H\n")
ucret = 0
if boyut == "S":
    ucret += 15
elif boyut == "M":
    ucret += 15
elif boyut == "L":
    ucret += 25
    
if biber == "E":
    if boyut == "S":
        ucret += 2
    else:
        ucret += 3
        
if peynir == "E":
    ucret += 1
    
print("Toplam ücret $", ucret)