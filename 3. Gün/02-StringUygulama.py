website = "http://www.sadikturan.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır ?
result = len(course)
length = len(website)
print(result)

# 2- 'website' içinden www karakterlerini alın.
print(website[7:10])
# 3- 'website' içinden com karakterlerini alın.
print(website[length-3:length])
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın.
print(course[:15])
print(course[-15:])
# 5- 'course' ifadesindeki karakterleri tersten yazdırın.
print(course[::-1])
name, surname, age, job = 'Berkcan','Gümüşışık', 22, 'Öğrenci'
# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
result1 = "Benim adım "+ name+ " " + surname+ ", Yaşım "+ str(age) + " ve mesleğim "+ job
result2 = "Benim adım {0} {1}, Yaşım {2} ve mesleğim {3}.".format(name,surname,age,job) 
result3 = f'Benim adım {name} {surname}, Yaşım {age} ve "mesleğim" {job}.'
print(result1)
print(result2)
print(result3)

# 7- 'Hello world' ifadesindeki w harfini 'W' ile değiştirin.
s = "Hello World"
print(s.replace("w", "W"))

# 8- 'abc' ifadesini yan yana 3 defa yazdırın.
print("abc"*3)

# 9-  ' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterlerini silin.
print(" Hello World ".strip())
print(" Hello World ".lstrip())
print(" Hello World ".rstrip())

# 10- 'www.sadikturan.com' içindeki sadikturan bilgisi haricindeki her karakteri silin.
print("www.sadikturan.com".strip('w.com'))

# 11-  'course' karakter dizisinin tüm karakterlerini küçük harf yapın.
print(course.lower())
print(course.upper())

# 12 - 'website' içinde kaç tane a karakteri vardır ? (count('a'))
print(website.count("a"))

# 13 - 'website' "www" ile başlayıp com ile bitiyor mu?
print(website.startswith("www"))
print(website.endswith(".com"))

# 14 -  'website' içinde '.com' ifadesi var mı?
print(website.index("com"))
print(website.find("com"))

# 14- 'course' içindeki karakterlerin hepsi alfabetik mi? 
print(course.isalpha())

# 15 - 'Contents' ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
print("Contents".center(50, "*"))
print("Contents".ljust(50, "*"))
print("Contents".rjust(50, "*"))

# 16 -  'course' karakter dizisindeki tüm boşluk karakterlerini '-' ile değiştirin.
print(course.replace(" ", "-"))

# 17- 'Hello World' karakter dizisinin 'World' ifadesini 'There' olarak değiştirin
print("Hello World".replace("World","There"))

# 18-  'course' karakter dizisini boşluk karakterlerinden ayırın.
print(course.split(" "))