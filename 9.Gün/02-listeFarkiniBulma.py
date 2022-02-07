"""
Aşağıda bulunan listeleri birbirleriyle karşılaştırın ve birinci listede bulunan hangi sayıların ikinci 
listede olmadığını, ikinci listede bulunan hangi sayıların birinci listede olmadığını tespit edin.
birinci_liste= [1,2,4,8,101,203,568,784,45,63,52,89,45,36,21,410,23,56,78,45,14,459,125,456,98,96,621]
ikinci_liste= [1,2,8,101,568,45,63,21,52,21,410,78,459,96,103,460,452,602]
"""

birinci_liste= [1,2,4,8,101,203,568,784,45,63,52,89,45,36,21,410,23,56,78,45,14,459,125,456,98,96,621]
ikinci_liste= [1,2,8,101,568,45,63,21,52,21,410,78,459,96,103,460,452,602]

sayi = 1
for i in ikinci_liste:
    if(not i in birinci_liste):
        print("İkinci listede bulunup birinci listede bulunmayan ",sayi,". sayı :", i)
        sayi += 1