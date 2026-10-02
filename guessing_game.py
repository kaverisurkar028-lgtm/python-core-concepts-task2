import random
number = random.randint(1, 100)
print("Welcome! Guess number 1-100")
attempts = 0
while True:
    try:
        guess = int(input("Enter guess: "))
        attempts += 1
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print(f"Correct! You won in {attempts} attempts")
            break
    except:
        print("Enter valid number")
