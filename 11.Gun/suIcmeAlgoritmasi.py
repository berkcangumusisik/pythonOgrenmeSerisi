""" 
Bir kişinin günlük içmesi gereken su miktarını litre cinsinden bulunuz. Erkekler için kg * 0.04 , kadınlar içn kg*0.03  ile bir kişinin içmesi gereken su bulunabilir.
"""
def suHesapla(kg):
    erkekSu = kg * 0.04
    kadinSu = kg * 0.03
    cinsiyet = input("Cinsiyetinizi giriniz : ").lower()
    if(cinsiyet == "erkek"):
        print(erkekSu," Litre su içmelisiniz.")
    elif(cinsiyet == "kadın"):
        print(kadinSu," Litre su içmelisiniz.")

kg = float(input("Kaç kilogramsınız : "))
suHesapla(kg)