import random

number = random.randint(1, 100)
print(number)

difficulty = input("Choose the difficulty, Hard or Easy").lower()
lives = ""
if difficulty == "hard":
    lives = 5
elif difficulty == "easy":
    lives = 10

is_game_over = False

for i in range(0, lives):
    guess = int(input(f"Make a guess you have {lives} left !"))
    lives -= 1
    if guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    elif guess == number:
        print("That's correct!")
        break
if lives >= 0:
    print("You won !")
else:
    print("You lose!")
