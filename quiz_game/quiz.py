print("Enter to KBC")
playing = input("Do you want to play (yes / no) ??").lower()

if playing != "yes":
    quit()
   
print("Okay, let's get started !")
score =0

answer = input("What does CPU stands for ?").lower()
if answer == "centeral processing unit":
    print("Correct")
    score = score + 1
else :
    print("Incorrect !!")

answer = input("What does RAM stands for ?").lower()
if answer == "random access memory":
    print("Correct")
    score = score + 1
else:
    print("INCORRECT")

answer = input("What does GPU stand for?").lower()
if answer =="graphic processing unit":
    print("Correct !!")
    score = score + 1
else:
    print("Incorrect")
    
    
print("You got" + str(score) + " questions correct !")
print("You got "+str((score / 3)*100) + "%.")

