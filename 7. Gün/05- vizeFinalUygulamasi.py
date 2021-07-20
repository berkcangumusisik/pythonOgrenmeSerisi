""") Kullanıcıdan vize ve final notu isteyin. Girilen vize notunun %40’ı ve 
girilen finalnotunun ise %60’ı alınarak yıl sonu not ortalaması hesaplanacaktır. 
Bu notortalaması eğer 85 ve üzeri ise AA, 
75 ve 85 arasında ise BA, 
70 ve 75 arasında ise BB, 
65 ve 70 arasında ise CB, 
60 ve 65 arasında ise CC, 
55 ve 60 arasında ise DC,
50 ve 55 arasında ise DD olarak hesaplanacaktır. 
Bu öğrencinin yıl sonu toplam notu 50’nin altında ise FF ile dersten kalacaktır. 
Ayrıca öğrencinin final notu 50’nin altında ise direkt FF ile kalacaktır.
"""

print("*** VİZE - FİNAL HESAPLAYICIYA HOŞ GELDİNİZ ***")
vize = float(input("Vize notunuzu giriniz:"))
final = float(input("Final notunuzu giriniz:"))
ortalama = (vize*0.4) + (final*0.6)
print("Ortalama: " + str(ortalama))
if final >= 50:
    if ortalama >= 85:
        print("AA alarak başarıyla geçtiniz.")
    elif ortalama >= 75:
        print("BA alarak başarıyla geçtiniz.")
    elif ortalama >= 70:
        print("BB alarak başarıyla geçtiniz.")
    elif ortalama >= 65:
        print("CB alarak başarıyla geçtiniz.")
    elif ortalama >= 60:
        print("CC alarak başarıyla geçtiniz.")
    elif ortalama >= 55:
        print("DC alarak başarıyla geçtiniz.")
    elif ortalama >= 50:
        print("DD alarak başarıyla geçtiniz.")
    else:
        print("FF alarak kaldınız.")
        
else:
    print("FF alarak kaldınız.")