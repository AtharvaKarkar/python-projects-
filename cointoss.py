import random

tries = 0
heads = 0
while tries < 20:
    tries += 1
    coin = random.randint(1, 2)
    if coin == 1:
        heads += 1
        print("Heads")
    if coin == 2:
        print("Tails")
total = tries
print("Total heads ".format(heads))
print("Total tails ".format(tries - heads))
print(total)
