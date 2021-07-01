# PYTHON TARİHÇESİ

- Geliştirilmeye 1990 yılında Guido van Rossum tarafından Amsterdam'da başlanmıştır.
- İsmini birçok kişi yılandan aldığını sansada Guido van Rossum'un sevdiği, Monty Python adlı altı kişilik bir İngiliz komedi grubunun Monty Python's Flying Circus adlı gösterisinden almıştır.
- 1994 yılında Python 1.0 kullanıma sunuldu.
- 2000 yılında Python 2.0 sürümü kullanıma sunuldu.
- 2008 yılında Python 3.0 sürümü kullanıma sunuldu.

![https://www.cozumpark.com/wp-content/uploads/2020/11/guido-van-rossum-1200x675-1.jpg](https://www.cozumpark.com/wp-content/uploads/2020/11/guido-van-rossum-1200x675-1.jpg)

Guido  van Rossum

# NEDEN PYTHON?

![https://www.iienstitu.com/uploads/online-egitim/python-egitimi-kursu_w380_h300_op.jpg](https://www.iienstitu.com/uploads/online-egitim/python-egitimi-kursu_w380_h300_op.jpg)

- Genel amaçlı bir dildir.
- Açık kaynak kodludur.
- Yorumlanabilir bir dildir.
- Yüksek seviyeli bir dildir.
- Dinamik tip tanımlamalı bir dildir.
- Birçok platformda çalışma imkanı sunar. Grafik , veritabanı , oyun yapay zeka vb
- Modüler
- Nesne yönelimlidir.
- Öğrenmesi kolaydır.

Pythonu [https://www.python.org/downloads/](https://www.python.org/downloads/)  sitesinden rahatlıklar kurabilirsiniz.

# PYTHON KODLARKEN DİKKAT EDİLECEKLER

- Python kodları yukarıdan aşağıya ve soldan sağa doğru okunur.
- Büyük küçük harf duyarlı bir dildir.
- Her şey nesnedir.
- Girinti boşluğu 4 karakterdir.
- Pythonda satır sonlarına ; konmaz.
- Python kodlarımızı .py uzantılı dosyalarda saklarız.

## YORUM SATIRLARI

Python’da # işareti kullanıldığı satırı yorum satırı yapar. Ayrıca """ """" arasına yazılacak yazıların tamamı yorum satırı olacaktır.

Yorum satırlarına neden ihtiyaç duyuyoruz biz dediğim oluyor ama çok büyük faydası var. Kod çalışırken işe yaramaz ama biz yazılımcılar arası haberleşmeyi, kodda neler yapmamız gerektiği gibi birçok konuda kullanımı mevcuttur. **Kısaca yorum satırları kodu etkilemez ve kod hakkında bilgilendirmeyi sağlar.**
```python
# Bu bir tekli yorum satırdır.

"""
Bu bir çoklu yorum satırıdır.
Birden fazla satırı yorum satırı yapar.
"""
```
## PRINT FONKSİYONU

Print fonksiyonu ekrana baskı yapmayı sağlar. 

*Print fonksiyonu kullanılırken yazılacak ifade print() içine yazılır.* 

*String ifadeler tek tırnak, çift tırnak ya da üç tırnak içinde yazılır.*

*Sayısal ifadeleri direkt olarak parantez içinde yazılabilir.*
```python
print("Merhaba Dünya") #Merhaba Dünya çıktısı verir.
print(2) #2 çıktısını verecektir.
```




# VERİ TÜRLERİ

### 1.STRING VERİ TÜRÜ

Metinsel ifadeleri içerir. Harfler, kelimeler, cümleler, metinler ve paragraflar bu gruba girer.

Bir ifade tırnak  ifadesi içine yazılmışsa string olarak değerlendirilir. 

Çift tırnak ya da tek tırnak olması önemli değildir.Eğer tek tırnak ile başladıysa tek tırnak, çift tırnak ile başladıysa çift tırnakla biter.

String ifadeler + operatörü ile birleştirme işlemi yapılabilir.

String ifadelerde çarpı koyarsanız ekrana o kadar o string ifadeyi bastırır.

```python
print("Merhaba") #Merhaba
print('Python öğreniyorum.') #Python öğreniyorum.
print("Ben bir BÖTE öğrencisiyim" + " ama yazılımcı olmak istiyorum.") #Ben bir BÖTE öğrencisiyim ama yazılımcı olmak istiyorum.
print("python "*10) #python python python python python python python python python python

```


### 2. SAYISAL VERİ TÜRLERİ

***a.integer veri türü***

Tam sayıları ifade eder. Mesela 5,12, 0 ,22, -431...

 b***.float veri türü***

Ondalıklı sayıları ifade eder. 5.3  7.8 0.0 -14.2 ....
```python
print(5)
print(40)
print(-40)

print(4.2)
print(0.0)
print(-14.2)
```

### 3.BOOLEAN VERİ TÜRÜ

İki değeri vardır ya true(1) ya da false(0) değerini dönderir.

Genellikle mantıksal ifadelerde yer verilir.


