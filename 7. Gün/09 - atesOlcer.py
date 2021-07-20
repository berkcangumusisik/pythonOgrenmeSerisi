"""
Bir AVM'ye ateş ölçer programı yazmalısınız.
Kullanıcıya ateşini sorun daha sonra ateşinin derecesine göre AVM'ye 
girip-giremeyeceğini kullanıcıya belirtin. 
Program sonunda şöyle bir çıktı elde etmelisiniz:
"Ateşiniz 39 derece. AVM'ye Giremezsiniz!"
"""

print("*** Ateş Ölçer Uygulamasına Hoş Geldiniz ***")
ates = float(input("Ateşinizi giriniz:"))
if ates >= 37.5:
    print("Ateşiniz " + str(ates) + " derece. AVM'ye giremezsiniz.")
else:
    print("Ateşiniz " + str(ates) + " derece. AVM'ye girebilirsiniz. Maske , mesafe ve temizliğe dikkat ediniz.")