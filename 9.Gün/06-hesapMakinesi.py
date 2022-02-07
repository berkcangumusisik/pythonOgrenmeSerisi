menu = """
1.Toplama
2.Çıkarma
3.Çarpma
4.Bölme
5.Karesini hesaplama
6.Karekök Hesaplama
q çıkış
"""

print("********** Hesap Makinesine Hoş Geldiniz *********")
print(menu)

while True:
    secim = input("Yapmak istediğiniz işlemi seçiniz : ")
    if secim == "q":
        print("Hesap makinesi sonlandırıldı.")
        break
    elif secim == "1":
        sayi1 = int(input("1.sayıyı giriniz :"))
        sayi2 = int(input("2.sayıyı giriniz :"))
        print(f"{sayi1} + {sayi2} = {sayi1 + sayi2}")
    elif secim == "2":
        sayi1 = int(input("1.sayıyı giriniz :"))
        sayi2 = int(input("2.sayıyı giriniz :"))
        print(f"{sayi1} - {sayi2} = {sayi1 - sayi2}")
    elif secim == "3":
        sayi1 = int(input("1.sayıyı giriniz :"))
        sayi2 = int(input("2.sayıyı giriniz :"))
        print(f"{sayi1} * {sayi2} = {sayi1 * sayi2}")
    elif secim == "4":
        sayi1 = int(input("1.sayıyı giriniz :"))
        sayi2 = int(input("2.sayıyı giriniz :"))
        print(f"{sayi1} / {sayi2} = {sayi1 / sayi2}")
    elif secim == "5":
        sayi1 = int(input("1.sayıyı giriniz :"))
        sayi2 = int(input("2.sayıyı giriniz :"))
        print(f"{sayi1} ** {sayi2} = {sayi1 ** sayi2}")
    elif secim == "6":
        sayi1 = int(input("1.sayıyı giriniz :"))
        print(f"{sayi1} sayisinin karekökü : {sayi1 * (1/2)}")
    else:
        print("Yanlış seçim yaptınız.")
