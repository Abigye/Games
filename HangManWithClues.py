import random

#prints scaffold
def print_scaffold(guesses, word):
    if (guesses == 0):
        print ("_________\n|	|\n|\n|\n|\n|\n|________")
    elif(guesses == 1):
        print ("_________\n|      |\n|      O\n|\n|\n|\n|________")
    elif (guesses == 2):
        print ("_________\n|      |\n|      O\n|      |\n|      |\n|\n|________")
    elif (guesses == 3):
        print ("_________\n|      |\n|      O\n|     \|\n|      |\n|\n|________")
    elif (guesses == 4):
        print ("_________\n|      |\n|      O\n|     \|/\n|      |\n|\n|________")
    elif (guesses == 5):
        print ("_________\n|      |\n|      O\n|     \|/\n|      |\n|     /\n|________")
    
    elif (guesses == 6):
        print ("_________\n|      |\n|      O\n|     \|/\n|      |\n|     / \ "+"\n|________")
        print ("\n")
        print ("The word was %s." % word)
        print ("\n")
        print ("\nYOU LOSE! TRY AGAIN!")
        print ("\nWould you like to play again, type y for yes or n for no?")
        again = str(input("> "))
        again = again.lower()
        if again == "y":
            hangMan()
        return

#selectng a random word to be guessed    
def selectingWord():
    lis = []
    tup_list= []
    file = open("text.txt")
    words = file.readlines()
    for word in words:
        line  = word.strip("\n")
        line = line.split("-")
        tup_list.append(tuple(line))
    tup_list =[(item[0].lower(), item[1].lower()) for item in tup_list]
    myTuple = random.choice(tup_list)
    return myTuple
   
# hangman game set up
def hangMan():
    guesses = 0
    selectedWord,meaning = selectingWord()
    selectedWord_list = list(selectedWord)
    guessing = "*" * len(selectedWord)
    guessing_list = list(guessing)
    new_guessing = list(guessing)
    guessed_list = []

    print("\nLet's play HangMan!!!\n")
    print_scaffold(guesses,selectedWord)
    print ("\n")
    print("Another word for " + meaning + '\n')
    print ("" + ' '.join(guessing_list))
    print ("\n")
    print ("Guess a letter.\n")

    while guesses < 6:
        guess = str(input("> "))
        guess = guess.lower()

        if len(guess) > 1:
            print ("Enter one letter at time.")
        elif guess == "":
            print("Bored already? Enter one letter at a time.")
        elif guess in guessed_list:
            print("Already guessed that! Here is what you've guessed: " )
            print(' '.join(guessed_list))
        else:
            guessed_list.append(guess)
            i = 0
            while i < len(selectedWord):
                if guess == selectedWord[i]:
                    new_guessing[i] = selectedWord_list[i]
                i = i + 1
                
            if new_guessing == guessing_list:
                print("Letter not in the word!")
                guesses = guesses + 1
                print_scaffold(guesses,selectedWord)

                if guesses < 6:
                      print("Guess Again.")
                      print(' '.join(guessing_list))
                      
            elif selectedWord_list != guessing_list:
                    guessing_list = new_guessing[:]
                    print(' '.join(guessing_list))

                    if selectedWord_list == guessing_list:
                         print ("\nYOU WIN!"+"\n"+"\nWouldyou like to play again?"+"\nType y for yes or n for no")
                         again = str(input("> "))
                         if again == "y":
                            hangMan()
                         quit()

                    else:
                        print("Great Guess :)")

hangMan()
