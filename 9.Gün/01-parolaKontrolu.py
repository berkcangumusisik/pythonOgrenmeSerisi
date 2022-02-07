""" 
Kullanıcıdan bir parola isteyin. Girilen parolanın 3 ile 8 karakter uzunluğunda olup-olmadığını kontrol edin. 
Aynı zamanda kullanıcının bir parola girdiğinden emin olun. Girilen parola 3 karakterden az ya da 
8 karakterden uzun ise ya da kullanıcı hiçbir parola girmemişse kullanıcıya gerekli uyarıları verin. 
Programınız şartların sağlandığı bir parola belirlenene kadar devam etsin. 
Şartların sağlandığı bir parola belirlendiğinde 
ise programı break deyimi ile sonlandırın. Program sonunda şöyle bir çıktı elde etmiş olmalısını:
parola belirleyin: 45
parola 8 karakterden uzun 3 karakterden kısa olmamalı
parola belirleyin:
"""

print("*********Formumuza Hoş Geldiniz**********")
while True:
    parola = input("Lütfen parolanızı giriniz :")
    if not parola:
        print("Parola boş bırakılamaz.")
    elif (len(parola) in range(3,9)):
        print("Parolanız başarıyla oluşturuldu.\nLütfen not alınız : ",parola)
        break
    else:
        print("Parolanız 8 karakterden uzun 3 karakterden kısa olmalıdır.")

        