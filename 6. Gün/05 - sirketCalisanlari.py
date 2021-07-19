"""# Sözlükleri kullanarak bir şirket çalışanları indeksi oluşturun. Bu isim indeksinde kişilerin isimleri key, kişilerin şu 
bilgileri de value olmalı: memleket, yaş, görev. Burada kullanacağımız value liste olmalı. 
Daha sonra bir isim sorgulama ekranı gibi kullanıcıya kimin bilgilerini görüntülemek istediğini 
sorun ve sorgulanan kişinin ekranda gösterilmesini sağlayın. Proje sonunda elde edeceğiniz çıktı şu şekilde olmalı:
Lütfen bilgilerini görüntülemek istediğiniz çalışanın ismini girin: Mehmet Yağız
Mehmet Yağız= Memleket: Adana Yaş: 40 Görev: Direktör
"""

sirketCalisani = {
    "Mehmet Yağız" : ["Adana","40","Direktör"],
    "Berkcan Gümüşışık" : ["Ankara","22","Stajyer"],
    "Ahmet Tozkoparan" :["İstanbul","32","Müdür"]
}

kisi = input("Lütfen bilgilerini görüntülemek istediğiniz çalışanın ismini girin:")
print(kisi + " = Memleket:" + sirketCalisani[kisi][0] + " Yaş:" + sirketCalisani[kisi][1] + " Görev:" + sirketCalisani[kisi][2])