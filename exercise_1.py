#A simple game where the user tries to guess a randomly generated number within a range.
import random

print(" Naruchnik za gambling addicts")

print("Namislih si chislo ot 1 do 50... ")


secret = random.randint(1, 50)
attempts = 0

while True:
    guess = input("Probvai: ")
    if not guess.isdigit():
        print("Aide da e chislo!")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("Probvai po-visoko!")
    elif guess > secret:
        print("Tvurde visoko, de! po-nisko?")
    else:
        print(f" Yay! Edvam uspq sled {attempts} opita!") 
        break

print("Aide, chao")



