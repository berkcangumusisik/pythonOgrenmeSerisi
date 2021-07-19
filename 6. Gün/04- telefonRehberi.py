"""
Sözlükleri Kullanarak Bir Telefon Rehberi Yazın. Bu rehberde kullanıcıya kimin telefonunu görüntülemek istediğini 
sorun ve kullanıcının girdiği isme göre o kişinin telefon numarasını yazdırın. Proje sonunda elde edeceğiniz çıktı 
şuna benzer olmalı:
Lütfen numarasını öğrenmek istediğiniz kişinin adını girin: Ahmet
Ahmet isimli kişinin numarası şu şekildedir: 0532 862 98 47
"""

telefonRehberi ={
    "Ahmet" : "0532 862 98 47",
    "Mehmet": "0533 863 98 47",
    "Ayşe": "0534 864 98 47"
}

kisi = input("Lütfen numarasını öğrenmek istediğiniz kişinin adını girin:")
print(kisi +" isimli kişinin numarası şu şekildedir: " + telefonRehberi[kisi])