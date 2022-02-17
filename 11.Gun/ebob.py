# EBOB hesaplayan bir fonksiyon yazınız.

def ebob(a,b):
    i = 1
    ebob = 1
    while(i<= a and i<=b):
        if(a % i == 0 and b %i == 0):
            ebob = i
        i += 1
    return ebob    
sayi1 = int(input("Birinci sayıyı giriniz : "))
sayi2 = int(input("İkinci sayıyı giriniz : "))
print("EBOB : ",ebob(sayi1,sayi2))