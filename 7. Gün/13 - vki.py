"""Talimatlar
Bir kullanıcının kilosuna ve boyuna göre Vücut Kitle İndeksini (BMI) yorumlayan bir program yazın.

BMI değerine göre BMI yorumunu onlara söylemelidir.

18,5'in altında zayıflar
18,5'in üzerinde ancak 25'in altında normal bir ağırlığa sahipler
25'in üzerinde ama 30'un altında biraz fazla kilolular
30'un üzerinde ama 35'in altında obezler
35'in üzerinde olanlar klinik olarak obezdir.


BMI, bir kişinin ağırlığının (kg olarak) boyunun karesine (m olarak) bölünmesiyle hesaplanır:

Uyarı sizi gerektiğini yuvarlamak en yakın tam sayıya sonucu. Yorum mesajının, yukarıdaki yorumlardan kalın harflerle yazılmış kelimeleri içermesi gerekir. örneğin zayıf, normal kilolu, fazla kilolu, obez, klinik olarak obez .

Örnek Giriş
weight = 85
height = 1.75
Örnek Çıktı
85 ÷ (1.75 x 1.75) = 27.755102040816325

Your BMI is 28, you are slightly overweight.
"""

kg = float(input("Kilonuzu kilogram cinsinden giriniz:"))
m = float(input("Boyunuzu metre cinsinden giriniz:"))
vki =round(kg/m**2)
if vki < 18.5:
    print("Vücut kitle indeksiniz:",vki," zayıfsınız.")
    
elif vki < 25:
    print("Vücut kitle indeksiniz:",vki," normal kilodasınız.")
    
elif vki < 30:
    print("Vücut kitle indeksiniz:",vki," kilonuzun biraz üzerindesiniz.")

elif vki < 35:
    print("Vücut kitle indeksiniz:",vki," obezsiniz.")
    
else:
    print("Vücut kitle indeksiniz:",vki," klinik obezsiniz.")