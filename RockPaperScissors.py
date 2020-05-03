import random
   
def game():
    total_count = 0
    user_count = 0
    computer_count = 0
    while total_count <=10:
        List = ["Rock","Paper","Scissors"]
        computer = random.choice(List)
        print ("Rock , Paper, Scissors ?")
        player = input ()
        print(f'You played {player}, the computer played {computer}')
        if player == computer:
            print("It's a tie!")
            computer_count = computer_count + 1
            user_count = user_count + 1
        elif player == "Rock":
           if computer == "Paper" :
               print ("Ouch! " + computer  + " covers " + player)
               computer_count = computer_count + 1
           else:
               print ("Good one there " + player + " smashes " + computer)
               user_count = user_count + 1
        elif player == "Scissors":
            if computer == "Rock":
               print("Ouch! " + computer + " smashes " + player)
               computer_count = computer_count + 1
            else:
               print("Smart ugh " + player + " cuts " + computer)
               user_count = user_count + 1
        elif player == "Paper":
            if computer == "Scissors":
               print ("Ouch! " + computer + " cuts " + player)
               computer_count = computer_count + 1
            else:
              print ("Nice move " + player + " covers " + computer)
              user_count = user_count + 1
        else :
             print("Invalid play")
             
        print(f'Computer: {computer_count} - You: {user_count}')
        print()
        total_count = total_count + 1
        if total_count == 10:
            if user_count > computer_count :
                print("You win")
            
            elif user_count < computer_count:
                print ("Be smart next time!")
            
            else:
                print("Wow, u are as smart as the computer!!")
                
            print ("\nWould you like to play again, type y for yes or n for no?")
            again = str(input("> "))
            again = again.lower()
            if again == "y":
                game()
            else:
                quit()

game()

