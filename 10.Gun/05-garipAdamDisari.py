"""Çok sayıda insanı ve çok sayıda grubu alan bir fonksiyon yazın. Kişiler gruplara eşit olarak bölünecektir 
(fazla kişiler olabilir). Çift grupları oluşturduktan sonra kalan kişi sayısını döndürür."""

def artaKalan(insanSayisi, grupNo):
    if insanSayisi < grupNo:
        return "Grup numarası insanların sayısına eşit veya daha az olmalıdır"
    return insanSayisi % grupNo

print(artaKalan(12,5))