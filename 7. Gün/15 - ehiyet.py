"""Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme  durumunu kontrol ediniz. 
Ehliyet alma koşulu en az 18 ve eğitim durumu  lise ya da üniversite olmalıdır. 
"""

isim = input('İsminiz: ')
yas = int(input('yaşınız: '))
egitim = input('Eğitim Durumunuz: ')

if (yas>=18):
    if (egitim=='lise' or egitim=='üniversite'):
        print(f'{isim} ehliyet alabilirsin.')
    else:
        print(f'{isim} ehliyet alamazsın eğitim durumun yetersiz.')
else:
    print(f'{isim} ehliyet alamazsın yaşın tutmuyor.')