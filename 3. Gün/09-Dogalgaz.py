"""  
Kullanıcının hangi ayda ne kadar doğalgaz faturası ödeyeceğini hesaplayan bir program yazın.
İlk olarak hangi ayı hesaplamak istediğini sorun daha sonra o ayda kaç metreküp doğalgaz kullandığını sorun.
Daha sonra ekrana "Şu ayda şu kadar fatura ödemeniz gerekiyor."
şeklinde bir cümle bastırın. (Doğalgazın metreküp fiyatı: 1.54).
"""

ay = input("Hangi ayda olduğunuzu yazınız:")
metrekup = input("Kaç metreküp doğalgaz harcadığınızı giriniz:")
birim = 1.54
fatura = float(metrekup) * float(birim)
print(ay , " ayında " , fatura ," TL fatura ödemeniz gerekiyor")