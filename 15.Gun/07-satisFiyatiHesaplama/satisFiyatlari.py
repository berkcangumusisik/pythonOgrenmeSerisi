def satisFiyati(satir):
    satir = satir[:-1]
    liste = satir.split(',')
    masraf = int(liste[1]) * 0.2
    vergi = int(liste[1]) * 0.18
    kar = int(liste[1]) * 0.25
    sonSatisFiyati = int(liste[1]) + masraf + vergi + kar
    return "Ürün: " + liste[0] + " || Satış Fiyatı: " + str(sonSatisFiyati) + "\n"
with open("Maliyetler.txt","r+",encoding="utf-8") as file:
    for i in file:
        urunler = []
        urunler.append(satisFiyati(i))
        with open("SatisFiyatlari.txt","a",encoding="utf-8") as file2:
            file2.writelines(urunler)