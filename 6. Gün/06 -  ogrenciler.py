"""5 öğrenciden oluşan bir öğrenci not sözlüğü oluşturun. Bu sözlükte 
öğrencilerin notları value olarak bir listede toplansın.
Kullanıcıya hangi öğrencinin notlarını görmek istediğini sorun. 
Öğrencinin notu görüntülendiğinde program sonunda şöyle bir çıktı elde etmelisiniz:
Lütfen notlarını görmek istediğiniz öğrencinin adını girin: Mehmet
Mehmet isimli öğrencinin 1.Sınav Notu:72
                              2.Sınav Notu:66
                              3.Sınav Notu:48
Not Ortalaması: 62.0
"""
ogrenciler = {
    "Mehmet":[72, 66, 48],
    "Berkcan": [88, 96, 100],
    "Ahmet": [70, 50, 40],
    "Sude": [92, 33, 78]
}
ogrenci = input("Lütfen notlarını görmek istediğiniz öğrencinin adını girin:")
ortalama = (ogrenciler[ogrenci][0] + ogrenciler[ogrenci][1] +ogrenciler[ogrenci][2])/3
print(
    ogrenci + " isimli öğrencinin 1.Sınav Notu: " + str(ogrenciler[ogrenci][0])+
                              " 2.Sınav Notu: " + str(ogrenciler[ogrenci][1]) +
                              " 3.Sınav Notu: " +  str(ogrenciler[ogrenci][2]) +
                              " Ortalama: " + str(ortalama)
    
    )