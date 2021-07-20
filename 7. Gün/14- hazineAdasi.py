print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("*** Hazine Adasına Hoş Geldiniz ***")
print("'Görevin hazineyi bulmak.")
ilkSecim = input("Bir yol ayrımındasınız. Nereye gitmek istersiniz? 'Sol' ya da 'Sağ' yazın\n")
if ilkSecim =="Sol":
    print("Güvenle bir göle geldiniz. İlk aşamayı başarıyla tamamladınız")
    ikinciSecim = input("Gölün ortasında bir ada var. Tekne beklemek için \"bekle\" yazın, yüzerek geçmek için \"yüzme\" yazın\n")
    if ikinciSecim == "bekle":
        print("Adaya zarar görmeden vardınız.")
        ucuncuSecim = input("3 kapılı bir ev var. Kapılardan Biri kırmızı, biri sarı ve biri mavi. Bir kapıyı seçiniz\n")
        if ucuncuSecim == "kırmızı":
            print("Ateşle dolu bir oda. Oyun Bitti")
        elif ucuncuSecim == "mavi":
            print("hayvanların odasına girdiniz. Oyun Bitti")
        elif ucuncuSecim == "sarı":
            print("Hazineyi buldunuz. Kazandınız!")
            print("Hazine Adasını oynadığınız için teşekkür ederiz!")
    elif  ikinciSecim == "yüzme":
        print("Kızgın bir alabalık tarafından saldırıya uğradınız. Oyun Bitti.")
    
elif ilkSecim == "Sağ":
    print("Deliğe düştünüz. Oyun Bitti")
else: 
    print("Sözdizimi Hatası") 