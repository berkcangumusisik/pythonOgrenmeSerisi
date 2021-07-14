# 1-  "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar = ['Bmw','Mercedes','Opel','Mazda']
# 2-  Liste Kaç elemanlıdır ?
print(len(arabalar))
# 3-  Listenin ilk ve son elemanı nedir ?
print(arabalar[0])
print(arabalar[-1])
# 4-  Mazda değerini Toyota ile değiştirin.
arabalar[-1]= 'Toyota'
print(arabalar)
# 5-  Listenin -2 indeksindeki değer nedir ?
print(arabalar[-2])
# 6-  Listenin ilk 3 elemanını alın.
print(arabalar[:3])
# 7-  Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ["Toyota","Renault"]
print(arabalar)
# 8-  Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
ekle = arabalar + ["Audi","Nissan"]
print(ekle)
# 9- Listenin son elemanını silin.
del arabalar[-1]
print(arabalar)
# 10- Liste elemanlarını tersten yazdırınız.
print(arabalar[::-1])
# 11- Aşağıdaki verileri bir liste içinde saklayınız. 

      # studentA: Yiğit Bilgi 2010, (70,60,70)
      # studentB: Sena Turan  1999, (80,80,70)
      # studentC: Ahmet Turan 1998, (80,70,90) 

studentA = ['Yiğit','Bilgi',2010,[70,60,70]]
studentB = ['Sena','Turan',1999,[80,80,70]]
studentC = ['Ahmet','Turan',1998,[80,70,90]]

# 12- Liste elemanlarını ekrana yazdırınız.

result1 = studentA[0]
result2 = studentB[1]
result3 = studentC[3][1]

result4 = f"{studentA[0]} {studentA[1]} {2019-studentA[2]} yaşında ve not ortalaması {(studentA[3][0] + studentA[3][1] + studentA[3][2])/3}"
print(result4)


  
names = ['Ali','Yağmur','Hakan','Deniz']
years = [1998, 2000, 1998, 1987]

# 13-  "Cenk" ismini listenin sonuna ekleyiniz.
names.append('Cenk')
print(names)
# 14-  "Sena" değerini listenin başına ekleyiniz.
names.insert(0,"Sena")
print(names)
# 15-  "Deniz" ismini listeden siliniz.
names.pop(-2)
print(names)

# 16-  "Ali" listenin bir elemanı mıdır ?
print(names.index("Ali"))
# 17-  Liste elemanlarını ters çevirin.
names.reverse()
print(names)
# 18-  Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)
# 19-  years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)
# 20-  str = "Chevrolet,Dacia" karakter dizisini listeye çeviriniz.
str = "Chevrolet,Dacia" 
print(str.split(","))

# 21- years dizisinde kaç tane 1998 değeri vardır ?
print(years.count(1998))

# 22- years dizisinin tüm elemanlarını siliniz.
years.clear()
print(years)
# 13- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.

markalar = []

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

marka = input("marka: ")
markalar.append(marka)

print(markalar)