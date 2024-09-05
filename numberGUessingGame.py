from art import logo
import random

random_number = random.randint(1, 100)
healths = 0

# Zorluk seçimi fonksiyonu
def difficulty_choose(difficulty):
    global healths  # Fonksiyonun dışında tanımlanan 'healths' değişkenini kullanmak için global yapıyoruz.
    
    if difficulty == "easy":
        healths = 10
    elif difficulty == "medium":
        healths = 7
    elif difficulty == "hard":
        healths = 5

# Sayı tahmin fonksiyonu
def guessing_number():
    global healths  # 'healths' değişkenini fonksiyon içinde değiştirebilmek için global yapıyoruz.
    
    print(logo)
    print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    
    # Zorluk seçimi burada yapılıyor ve haklar belirleniyor
    difficulty = input("Choose a difficulty. Type 'easy', 'medium', or 'hard': ").lower().strip()
    difficulty_choose(difficulty)
    
    # Tahmin döngüsü
    while healths > 0:
        guess = int(input("Make a guess: "))  # Tahmin alınıyor ve int'e dönüştürülüyor

        if guess == random_number:
            print("You got it! The answer is {}".format(random_number))
            return  # Doğru tahmin edildiğinde oyundan çıkıyoruz

        elif guess > random_number:
            print("Too high.")
        elif guess < random_number:
            print("Too low.")

        # Her tahmin sonrası bir hak eksiliyor
        healths -= 1
        print(f"Remaining attempts: {healths}")

        if healths == 0:
            print(f"You've run out of guesses. The number was {random_number}.")
            return  # Oyun bittiğinde fonksiyonu sonlandırıyoruz

# Oyunu başlatıyoruz
guessing_number()
