import random

guess = 0
attempt = 0

target_num = random.randint(1,100)



while guess != target_num:
    guess = int(input("Guess the number: \n"))
    attempt = attempt + 1 
    if guess < target_num:
        print("Too low, try again !!")
    else:
        print("Too high, try again") 
        
print(f"Congrats, you gueesed the number right {target_num} in {attempt} attempts. ")
