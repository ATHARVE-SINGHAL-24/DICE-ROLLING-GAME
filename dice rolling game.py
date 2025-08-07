#dice rolling game 

# print("welcome to dice rolling game!")
# import random

# while True:
#     answer=str(input("do you want to roll the dice?(y/n): "))
#     if(answer=="y"):
#         die1=random.randint(1,6)
#         print(f"({die1})")
#     elif(answer=="n"):
#         print("thanks for playing")
#         break
#     else:
#         print("invalid choice!")
    





#level 2


print("welcome to dice rolling game!")

number_of_die=int(input("enter the number of die you want to roll:"))
print("OK,LET'S START THE GAME")
if(number_of_die==1):
    import random

    while True:
        answer=str(input("do you want to roll the dice?(y/n): "))
        if(answer=="y"):
            die1=random.randint(1,6)
            print(f"({die1})")
        elif(answer=="n"):
            print("thanks for playing")
            break
        else:
            print("invalid choice!")


if(number_of_die==2):

    import random

    while True:
        answer=str(input("do you want to roll the dice?(y/n): "))
        if(answer=="y"):
            die1=random.randint(1,6)
            die2=random.randint(1,6)
            print(f"({die1,die2})")
        elif(answer=="n"):
            print("thanks for playing")
            break
        else:
            print("invalid choice!")

if(number_of_die==3):
    import random

    while True:
        answer=str(input("do you want to roll the dice?(y/n): "))
        if(answer=="y"):
            die1=random.randint(1,6)
            die2=random.randint(1,6)
            die3=random.randint(1,6)
            print(f"({die1,die2,die3})")
        elif(answer=="n"):
            print("thanks for playing")
            break
        else:
            print("invalid choice!")

