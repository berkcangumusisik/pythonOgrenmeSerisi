import random
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def checkAnswer(answer, guess,turns):
    if guess > answer:
        print("Yüksek")
        return turns - 1
    elif guess < answer:
        print("Düşük")
        return turns - 1
    else:
        print("Tahmin doğru. Cevap: ", answer)

def setDifficulty():
    level = input("Bir zorluk seçin. 'Kolay' veya 'zor' yazın:")
    if level == "Kolay":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
        


def game():
    print(logo)
    print("Sayı Tahmin Oyununa Hoşgeldiniz")
    print("1 - 100 arasında sayı tutuyorum")
    answer = random.randint(1, 100)
    guess = 0
    turns = setDifficulty()
    while guess != answer:
        print(f"Sayıyı denemek için {turns} hakkınız kaldı")
        guess = int(input("Tahmininizi giriniz: "))
        turns = checkAnswer(guess, answer, turns)
        if turns == 0:
            print("Oyun bitti. Oyunu kaybettiniz.")
            return
        elif guess != answer:
            print("Tekrar tahmin edin.")

game()