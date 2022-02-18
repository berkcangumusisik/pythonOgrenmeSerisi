from cmath import log
from math import fabs


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alfabe = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def sezar(metin,anahtarSayisi,sifre_Turu):
    sonMetin = ""
    if sifreTuru == "decode":
        anahtarSayisi *= -1
    for harf in metin:
        if harf in alfabe:
            pozisyon = alfabe.index(harf)
            yeniPozisyon = pozisyon + anahtarSayisi
            sonMetin += alfabe[yeniPozisyon]
        else:
            sonMetin += harf
    print(f"Şifreleme Türünüz : {sifreTuru}")
    print(f"Son metin : {sonMetin}")
print(logo)
bittiMi = False
while not bittiMi:
    sifreTuru = input("Şifrelemek için 'encode' yazın, şifresini çözmek için 'decode' yazın:\n")
    mesaj = input("Mesajınızı giriniz:\n").lower()
    anahtar = int(input("Kaç harf atlanarak ilerlemek istersiniz:\n"))
    anahtar = anahtar % 26
    sezar(mesaj,anahtar,sifreTuru)
    tekrar = input("Bitirmek için 'Hayır' devam etmek için 'Evet' yazınız :\n ")
    if tekrar=="Hayır":
        bittiMi = True
        print("Görüşmek üzere!!!!")
    



    