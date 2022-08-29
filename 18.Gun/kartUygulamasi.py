# Kart sınıfı

# Kart sınıfından türetilen her bir nesne bir kart türünü temsil edecek.
# Kart sınıfının tip ve deger isminde 2 instance özelliği olsun. (tip:sinek deger:5)

# sinek5 = Kart("sinek","5")
# karoAs = Kart("karo","A")

# Kart sınıfının kartıGetir() ismindeki instance metodu kart bilgilerini yazdırsın.

# sinek5.kartıGetir() => sinek 5

# Deste sınıfı

# deste1 = Deste()

# kart tipleri   => karo,sinek,kupa,maça
# kart değerleri => A,2,3,4,5,6,7,8,9,10,J,Q,K

# Deste sınıfındaki kartlar listesine 52 kartı for ve list comphension ile ekleyiniz.
# Destede kalan kart sayısı için kartSayisi() isminde bir metot.
# Destedeki kartları karıştırmak için KartlariKaristir() isminde bir metot.
# kartDagit() ismindeki metot belirtilen adet kadar kartı dağıtmalıdır. Destedeki kalan kart sayısına dikkat.
# kartAt() ismindeki metot elden bir kart atmak için kullanılsın.

from random import shuffle

class Kart:
    def __init__(self,tip,deger):
        self.tip = tip
        self.deger = deger

    def __repr__(self):
        return f"{self.tip} {self.deger}"

class Deste:
    tipler = ["karo","sinek","kupa","maça"]
    degerler = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    def __init__(self):
        self.kartlar = [Kart(tip,deger) for tip in Deste.tipler for deger in Deste.degerler]

    def kartSayisi(self):
        return len(self.kartlar)

    def kartlariKaristir(self):
        if (self.kartSayisi()<52):
            raise ValueError("Deste bozulmadan kartları karıştırabilirsiniz.")
        shuffle(self.kartlar)

    def kartDagit(self,adet):
        kartSayisi = self.kartSayisi()
        if kartSayisi == 0:
            raise ValueError("Bütün kartlar dağıtıldı.")
        adet = min([kartSayisi,adet])
        kartlar = self.kartlar[-adet:]
        self.kartlar = self.kartlar[:-adet]
        return kartlar

    def kartAt(self):
        return self.kartDagit(1)[0]




deste1 = Deste()

deste1.kartlariKaristir()

print(deste1.kartAt())

print(deste1.kartDagit(5))
print(deste1.kartlar)
print(deste1.kartSayisi())
print(deste1.kartDagit(3))
print(deste1.kartSayisi())

print(deste1.kartlar)
