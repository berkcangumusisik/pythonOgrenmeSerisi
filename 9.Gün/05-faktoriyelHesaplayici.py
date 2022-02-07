print("---Faktöriyel hesaplama programına hoş geldiniz ---")
sayi = int(input("Faktöriyelini hesaplamak istediğiniz sayıyı yazınız : "))
faktoriyel = 1
for i in range(2, sayi+1 ):
    faktoriyel *= i
    
print(f"{sayi} sayısının faktöriyeli {faktoriyel} sayısıdır.")
    