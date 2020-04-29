# This is a word game
import random

# # Game setup
# print("Welcome to Hangman!")
# print("There are multiple difficulty settings shown below:")
# print("\t1. Beginner (10 lives)")
# print("\t2. Intermediate (8 lives)")
# print("\t3. Expert (6 lives)")
# print("\t4. Advanced (4 lives)")
# print("\t5. Insane (2 lives)")
#
# # Choose a difficulty level
# user_setting = input("Please choose a difficulty by typing its number: ")
#
# # # Establish a list of words that can be chosen for the game
# # with open("words.txt") as f:
# #     word_list = f.read().splitlines()
#
# # Inform the user of their selection
# if (str(user_setting) == "1"):
#     number_of_lives = 10
#     print("\nYou have chosen %s and will receive %d lives." % ("Beginner", number_of_lives))
# elif (str(user_setting) == "2"):
#     number_of_lives = 8
#     print("\nYou have chosen %s and will receive %d lives." % ("Intermediate", number_of_lives))
# elif (str(user_setting) == "3"):
#     number_of_lives = 6
#     print("\nYou have chosen %s and will receive %d lives." % ("Expert", number_of_lives))
# elif (str(user_setting) == "4"):
#     number_of_lives = 4
#     print("\nYou have chosen %s and will receive %d lives." % ("Advanced", number_of_lives))
# elif (str(user_setting) == "5"):
#     number_of_lives = 2
#     print("\nYou have chosen %s and will receive %d lives." % ("Insane", number_of_lives))
# else:
#     number_of_lives = 10
#     print("\nYou have made an invalid selection and will receive %d lives by default." % number_of_lives)


def print_scaffold(guesses, wd):  # prints the scaffold
    if (guesses == 0):
        print "_________"
        print "|	 |"
        print "|"
        print "|"
        print "|"
        print "|"
        print "|________"
    elif (guesses == 1):
        print "_________"
        print "|	 |"
        print "|	 O"
        print "|"
        print "|"
        print "|"
        print "|________"
    elif (guesses == 2):
        print "_________"
        print "|	 |"
        print "|	 O"
        print "|	 |"
        print "|	 |"
        print "|"
        print "|________"
    elif (guesses == 3):
        print "_________"
        print "|	 |"
        print "|	 O"
        print "|	\|"
        print "|	 |"
        print "|"
        print "|________"
    elif (guesses == 4):
        print "_________"
        print "|	 |"
        print "|	 O"
        print "|	\|/"
        print "|	 |"
        print "|"
        print "|________"
    elif (guesses == 5):
        print "_________"
        print "|	 |"
        print "|	 O"
        print "|	\|/"
        print "|	 |"
        print "|	/ "
        print "|________"
    elif (guesses == 6):
        print "_________"
        print "|	 |"
        print "|	 O"
        print "|	\|/"
        print "|	 |"
        print "|	/ \ "
        print "|________"
        print "\n"
        print "The word was %s." % wd
        print "\n"
        print "\nYOU LOSE! TRY AGAIN!"
        print "\nWould you like to play again, type 1 for yes or 2 for no?"
        again = str(raw_input("> "))
        again = again.lower()
        if again == "1":
            hangMan()
        return



def selectWord():
    file = open('words.txt')
    words = file.readlines()
    myword = 'a'
    while len(myword) < 4:  # makes sure word is at least 4 letters long
        myword = random.choice(words)
    myword = str(myword).strip('[]')
    myword = str(myword).strip("''")
    myword = str(myword).strip("\n")
    myword = str(myword).strip("\r")
    myword = myword.lower()
    return myword


def hangMan():
    guesses = 0
    word = selectWord()
    word_list = list(word)
    blanks = "_" * len(word)
    blanks_list = list(blanks)
    new_blanks_list = list(blanks)
    guess_list = []

    print "Let's play hangman!\n"
    print_scaffold(guesses, word)
    print "\n"
    print "" + ' '.join(blanks_list)
    print "\n"
    print "Guess a letter.\n"

    while guesses < 6:

        guess = str(raw_input("> "))
        guess = guess.lower()

        if len(guess) > 1:
            print "Stop cheating! Enter one letter at time."
        elif guess == "":
            print "Don't you want to play? Enter one letter at a time."
        elif guess in guess_list:
            print "You already guessed that letter! Here is what you've guessed:"
            print ' '.join(guess_list)
        else:
            guess_list.append(guess)
            i = 0
            while i < len(word):
                if guess == word[i]:
                    new_blanks_list[i] = word_list[i]
                i = i + 1

            if new_blanks_list == blanks_list:
                print "Your letter isn't here."
                guesses = guesses + 1
                print_scaffold(guesses, word)

                if guesses < 6:
                    print "Guess again."
                    print ' '.join(blanks_list)

            elif word_list != blanks_list:

                blanks_list = new_blanks_list[:]
                print ' '.join(blanks_list)

                if word_list == blanks_list:
                    print "\nYOU WIN!"
                    print "\nU are such a great guesser!"
                    print "\n"
                    print "Would you like to play again?"
                    print "Type 1 for yes or 2 for no."
                    again = str(raw_input("> "))
                    if again == "1":
                        hangMan()
                    quit()

                else:
                    print "Great guess! Guess another!"


hangMan()