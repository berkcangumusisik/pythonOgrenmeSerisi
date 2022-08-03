"""
Fantasya'da;

Her 7 saniyede bir doğum gerçekleşiyor.

Her 13 saniyede bir ölüm meydana geliyor.

Her 45 saniyede bir göç alınıyor.

Önümüzdeki 5 yıl sonraki popülasyonu hesaplamak için bir program yazın. Şu anki Fantasya nüfusunun 3.000.000 kişi, 1 yılda 365 gün olduğunu varsayın.

İpucu : Pythonda bölme işlemi için tam sayı bölme operatörünü (//) kullanabilirsiniz. Örneğin; 5//4=1 (1.25 değil), 10//4=2 (2.5 değil) 
"""
nufus = int(input("Nüfus : "))
saniye = 5 * 365 * 24 * 60 * 60
dogum = saniye // 7
olum = saniye // 13
goc_alim = saniye // 45
nufus_son = nufus + dogum + goc_alim - olum
print("5 yılın sonundaki toplam nüfus : ", nufus_son)