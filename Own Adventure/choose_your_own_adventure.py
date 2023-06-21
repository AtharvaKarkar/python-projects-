name = input("Enter your name: ")
print("Welcome", name,"to this adventure!!!")

answer = input("You are on a dirt road,it has come to an end and you can go left or right. Which way would you choose to go?").lower()

if answer == "left":
    answer = input("You come to a river,you can walk around it or swin across ?? Type walk to walk around and swim to swim across: ").lower()
    
    if answer == "swim":
        print("You can swim across and were eaten by an crocodile. WASTED!!!")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option.")
    
elif answer =="right":
    answer=input("You come to a bridge,it looks wobbly, do you want to cross it or head back (cross/back)?")
    if answer == "back":
        print("WASTED")
    elif answer == "cross":
        answer=input("You cross the bridge and meet a stranger. Will you talk to them (yes/no)?")
        
        if answer =="yes":
            print("You talk to the stranger and they give you DIAMOND. MISSION COMPLETED!!!")
        elif answer =="no":
            print("You ignore the stranger and they are offended now . WASTED !!")
        else:
            print("Not a valid option.")
    else:
        print("Not a valid option.")

else:
    print("Not a valid option. You lose.")
    
print("Thank you for trying",name)