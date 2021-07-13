""" 
aşağıdaki dilekçe örneğini kullanıcıdan aldığınız verileri ile tamamlayın.
TIP FAKÜLTESİ DEKANLIĞINA İSTANBUL .../.../20..

Konu:....

Gereğinin yapılmasını arz ederim. Saygılarımla,

Ad-Soyad:...

Adres Bilgileri:...

Telefon:...
"""

gun = int(input("Dilekçe günü giriniz: "))
ay = int(input("Dilekçe ayı giriniz: "))
yil = int(input("Dilekçe yılını giriniz: "))
konu = input("Dilekçe konusu giriniz: ")
name = input("İsim ve soyisim giriniz: ")
adres = input("Adres bilgilerinizi giriniz:")
telefon = input("Telefon numaranızı giriniz:")

print("TIP FAKÜLTESİ DEKANLIĞINA İSTANBUL " + str(gun) + "/"+str(ay)+"/20"+str(yil))
print("Konu:"+konu)
print("Gereğinin yapılmasını arz ederim. Saygılarımla,")
print("Ad-Soyad:"+name)
print("Adres Bilgileri:"+adres)
print("Telefon:"+telefon)
