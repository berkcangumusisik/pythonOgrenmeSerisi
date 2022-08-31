# Quiz App

# Question sınıfı
#   Instance Attributes
#       - text, choices, answer
#   Instance Methods
#       - q1.checkAnswer('python') => True ya da False

# Quiz sınıfı
#   Instance Attributes
#       - questions, questionIndex, score
#   Instance Methods
#       - getQuestion()         => questionIndex' e göre question nesnesi getirir.
#       - displayQuestion()     => getQuestion() ile alınan nesneyi gösterir.
#       - loadQuestion()        => Testi başlatır.
#       - displayScore()        => Score bilgisini gösterir.
#       - displayProgress()     => Testdeki ilerlemeyi gösterir. (5 sorunun 2.sorusundasınız.)


import random

class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self,answer):
        if answer not in self.choices:
            raise ValueError("hatalı bilgi")
        return self.answer == answer

class Quiz:
    def __init__(self,questions):
        self.questions = random.sample(questions, len(questions))
        self.questionIndex = 0
        self.score = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()

        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for q in question.choices:
            print("-" + q)

        answer = input('cevap: ')
        if (question.checkAnswer(answer)):
            self.score += 1
            print("tebrikler bildiniz.")

        self.questionIndex += 1
        self.loadQuestion()

    def loadQuestion(self):
        if len(self.questions) == self.questionIndex:
            self.displayScore()
        else:
            self.displayProgress()
            self.displayQuestion()

    def displayScore(self):
        print("Test Özetiniz".center(100,'*'))
        puan = 100 / len(self.questions)
        toplamPuan = round(self.score * puan)
        print(f"Toplam {len(self.questions)} sorunun {self.score} tanesini bildiniz.")
        print("Kazandığınız puan:", toplamPuan)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        print(f"Toplam {totalQuestion} sorunun {questionNumber}. sorusundasınız.".center(100,'*'))

q1 = Question("Hangisi string methodlarından birisi değildir? ",["len","upper","lowe","return"],"return")
q2 = Question("Python Jump programına kaç kişi kabul almıştır? ",["122","221","222","112"],"122")
q3 = Question("Hangisi YetGen liderlerinden biri değildir? ",["Berkcan","Çağla","Adem","Gaye"],"Gaye")

sorular = [q1,q2,q3]

quiz = Quiz(sorular)

quiz.loadQuestion()





