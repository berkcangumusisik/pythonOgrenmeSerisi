# Comment isminde bir sınıf oluşturunuz.
# Comment sınıfı username, text, likes, dislikes isminde özelliklere sahip olsun.
# 5 adet farklı comment oluşturup döngü yardımıyla yorumları ekrana yazdırınız.

class Comment:
    def __init__(self, username, text, likes=0, dislikes=0):
        self.username = username
        self.text = text
        self.likes = likes
        self.dislikes = dislikes

c1 = Comment("berkcan","güzel kurs")
c2 = Comment("ahmet","çok güzel kurs")
c3 = Comment("cinar","idare eder bir kurs", 50, 10)
c4 = Comment("ahmet","kursu beğenmedim")
c5 = Comment("berkcan","süper bir kurs olmuş",100)

comments = [c1,c2,c3,c4,c5]

for c in comments:
    print(f"{c.username}: {c.text}")
    print(f"likes: {c.likes} - dislikes: {c.dislikes}")