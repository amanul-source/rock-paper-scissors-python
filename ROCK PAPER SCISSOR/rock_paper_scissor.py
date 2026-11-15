import random
while True:
    print("==========ROCK PAPER SCISSOR=========")
    choices="ROCK","PAPER","SCISSOR"
    print("1. ROCK")
    print("2. PAPER")
    print("3. SCISSOR")

    user_choice=int(input("Enter your choice: "))

    if user_choice==1:
        user_selection="ROCK"
    elif user_choice==2:
        user_selection="PAPER"
    elif user_choice==3:
        user_selection="SCISSOR"
    else:
        print("invalid selection!!!!")
        exit()

    computer_choice=random.choice(choices)

    print("User choice:",user_selection)
    print("Computer choice:",computer_choice)

    if user_selection==computer_choice:
        print("Match draw!!!")      
    elif user_selection=="ROCK" and computer_choice=="SCISSOR":
        print("Winner!!!")
    elif user_selection=="PAPER" and computer_choice=="ROCK":
        print("Winner!!!")
    elif user_selection=="SCISSOR" and computer_choice=="PAPER":
        print("winnner!!!")
    else:
        print("you lose!!!")

    print("Do you want to play again (yes/No)")
    play_again=input("Enter your choice: ")
    if play_again.lower()=="no":
        break

 




   
    