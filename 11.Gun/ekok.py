# EKOK hesaplayan bir fonksiyon yazınız.
def ekok(a,b):
    i = 2
    ekok = 1
    while True:
        if(a % i == 0 and b % i == 0):
            ekok *= i
            a /= i
            b /= i
        elif(a % i == 0 and b % i != 0):
            ekok *= i
            a /= i
        elif(a % i != 0 and b % i == 0):
            ekok *= i
            b /= i
        else:
            i += 1
        if(a == 1 and b == 1):
            break
    return ekok
sayi1 = int(input("Birinci sayıyı giriniz : "))
sayi2 = int(input("İkinci sayıyı giriniz : "))
print("EKOK : ",ekok(sayi1,sayi2))