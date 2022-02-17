""" Bir duvar boyamaya karar verdiniz . Boya kutusunun üzerindeki talimatta, 1 kutu boyanın 5 metrekarelik bir duvarı boyayabileceği yazıyor . Rastgele bir duvar yüksekliği ve genişliği verildiğinde, kaç kutu boya satın almanız gerektiğini hesaplayın.
kutu sayısı = (duvar yüksekliği + duvar genişliği) ÷ kutu başına kaplama.

örneğin Yükseklik = 2, Genişlik = 4, Kapsama = 5
kutu sayısı = (2 * 4) ÷ 5 = 1.6
Ancak bir kutu boyanın 0,6'sını satın alamayacağınız için, sonuç 2 kutuya yuvarlanmalıdır .
"""

import  math
def boyama(yukseklik, genislik, kaplama):
    alan = yukseklik * genislik
    kutuSayisi = math.ceil(alan / kaplama)
    print(f"{kutuSayisi} kutu boyaya ihtiyacınız var.")
    
yukseklik = int(input("Yükseklik giriniz : "))
genislik = int(input("Genişlik giriniz : "))
kaplama = 5
boyama(yukseklik,genislik,kaplama)
