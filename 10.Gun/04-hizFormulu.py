"""
Fizikte, bir nesnenin sabit ivmeyle hareket ederken son hızını 
(veya hızını) bulmak için aşağıdaki denklem kullanılabilir:
vf = vi + at
burada:
vf= son hız
vi= ilk hız
a= hızlanma
t= zaman
İlk hız, ivme ve zaman verildiğinde, son hızı döndürecek bir fonksiyon yazın.
"""

vi=float(input("ilk hız değerini giriniz: "))
a=float(input("İvme değerini giriniz: "))
t=float(input("Zaman değerini giriniz: "))

def sonHiz(vi, a, t):
    vf=float(vi+a*t)
    print("son hız:",vf)


sonHiz(vi,a,t)