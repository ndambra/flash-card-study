import os.path
from os import path
import random

class IndexCard(object):
    def __init__(self,keyword):
        self.keyword = keyword

    def set_definition(self):
        print("\nWhat's the definition for {}: ".format(self.keyword))
        definit = input()
        self.definition = definit

    def change_definition(self, newDef):
        self.definition = newDef
        print("\n**Definition for '{}' changed successfully.".format(self.keyword))


def studyCards(indexCards):
    wrongGuesses = []
    count = 1
    # shuffle the list so it's in a different order each time
    random.shuffle(indexCards)
    print("\nAlright! Let's study those flash cards!\n")

    for card in indexCards:
        incorrect = True
        word = card.keyword
        print("{}. {}".format(count, card.definition))

        while incorrect:
            guess = input("\nWhat's the word? ")

            if guess == word:
                print("Correct! Next word...\n")
                incorrect = False
            else:
                print("\nIncorrect. Try again.")
                if word in wrongGuesses:
                    print("Check your spelling.")
                else:
                    wrongGuesses.append(word)
                # end else
            # end else
        # end while loop
        count += 1
    #end for loop
    results(wrongGuesses)


def editCard(indexCards):
    myCard = input("Which card would you like to edit? ")
    if cardExists(myCard, indexCards, False):
        yesNo = input("You would like to edit the definition for '{}'? ".format(myCard)).lower()
        if yesNo == "yes" or yesNo == "y":
            newDef = input("Enter the new definition: ")
            card.change_definition(newDef)
        elif yesNo == "no" or yesNo == "n":
            print("Okay then.")
        else:
            print("\nYou entered an invalid response and I don't feel")
            print("like validating for a right one and letting you")
            print("try again, so we are heading back to the main menu")
            print("and you can try again from there.")
            print("Remember: a yes or no question only needs a yes or no response")
        # end else
    else:
        print("I'm sorry, that word does not appear to be on any of the flash cards.")


def viewCard(indexCards):
    myCard = input("Which card would you like to review? ")
    if cardExists(myCard, indexCards, False):
        input("Press enter to view the definition for '{}'".format(myCard))
        print(card.definition)
    else:
        print("I'm sorry, that word does not appear to be on any of the flash cards.")


def results(wrongWords):
    if len(wrongWords) == 0:
        print("Well done! You got them all correct 1st try!")
    else:
        numWrong = len(wrongWords)
        print("You had trouble with these {} words:".format(numWrong))
        for word in wrongWords:
            print(word)
        # end for loop
        print("Be sure to go back and study those words some more.")
    # end else


def print_options():
    print()
    print("1. Study all cards.")
    print("2. Edit a definition.")
    print("3. View a specific card.")
    print("4. Add/remove a card")
    print("5. Quit.")


def shallWeStudy():
    while True:
        study = input("Shall we study? ").lower()
        if study == "yes" or study == "y":
            return True
        elif study == "no" or study == "n":
            print("Okay, maybe next time!")
            return False
        else:
            print("I'm sorry, yes or no are all I understand.")
        # end else
    # end while loop
    return False


def getOurWords():
    myKeywords = []
    while True:
        try:
            userChoice = int(input("Where to find study words? \n1. A file\n2. Enter my own\n3. Use testing\n\nAnswer: "))
        except ValueError:
            print("\nInvalid option. Try again.\n")
            continue
        if userChoice == 1:
            myKeywords = openWordsFromFile()
            if myKeywords == None:
                print("Something went wrong")
            else:
                break
            # end else
        elif userChoice == 2:
            print("Alright, let's make some flash cards!")
            done = False

            while not done:
                nextWord = input("Enter a word: ")
                myKeywords.append(nextWord)
                addMore = input("\nAdd another card? ").lower()

                if addMore == "no" or addMore == "n":
                    done = True
                # end if
            # end while loop
            break
        elif userChoice == 3:
            print("Ok, for testing purposes we will use some hard coded words.")
            myKeywords = ["class", "object", "instance", "def", "self", "inheritance",
                        "composition", "attribute", "is-a", "has-a"]
            break
        else:
            print("Please choose 1 or 2.\n")
        # end else
    # end while loop
    return myKeywords


def openWordsFromFile():
    myKeywords = []
    fileName = input("Enter file name > ")
    if path.exists(fileName):
        print("Looks like the file exists")
        file = open(fileName, "r")
        for word in file:
            myKeywords.append(word.strip())
        # end for loop
        file.close()
    else:
        print("Error: File does not  exist")
    # end else
    return myKeywords


def addRemove(indexCards):
    notDone = True
    while notDone:
        try:
            edit = int(input("\nChoose:\n1. Add a card\n2. Remove a card\n>> "))
        except ValueError:
            print("\nInvalid option. Try again.\n")
            continue
        if edit == 1:
            addCard(indexCards)
            notDone = False
        elif edit == 2:
            removeCard(indexCards)
            notDone = False
        else:
            print("Invalid choice.")
        # end else
    # end while loop

def addCard(indexCards):
    newWord = input("New word to add: ")
    if cardExists(newWord, indexCards, False):
        print("That word is already on a card!")
        print("No card added.")
    else:
        newCard = IndexCard(newWord)
        newCard.set_definition()
        indexCards.append(newCard)
        print("{} was added.".format(newWord))
    # end else


def removeCard(indexCards):
    checkWord = input("Which word would you like to remove? ")
    if cardExists(checkWord, indexCards, True):
        print("The card for word '{}' was successfully removed.".format(checkWord))
    else:
        print("Sorry, that word doesn't seem to be among any of our cards.")
    # end else


def cardExists(myWord, indexCards, remove):
    for card in indexCards:
        if myWord == card.keyword:
            if remove:
                indexCards.remove(card)
            # end if
            return True
        # end if
    # end for loop
    return False



#### START MAIN THREAD ####

myIndexCards = []
options = {1:studyCards, 2:editCard, 3:viewCard, 4:addRemove}

myKeywords = getOurWords()
letsStudy = shallWeStudy()

while letsStudy:
    # Make the user enter in the definition as a way to start
    # studying the words/definitions
    if len(myIndexCards) == 0:
        print("\nHelp me make the flash cards.")
        print("I have the words, just give me the definitions.")
        for word in myKeywords:
            newCard = IndexCard(word)
            newCard.set_definition()
            myIndexCards.append(newCard)
        # end for loop
    # end if

    # We will allow the user to study all the cords, edit a card, or
    # take a look at a specific card
    print_options()
    try:
        choice = int(input("\nWhat would you like to do? "))
    except ValueError:
        print("\nInvalid option. Try again.\n")
        continue
    if choice == 5:
        print("You chose to quit. See you next time!")
        letsStudy = False
    elif 0 < choice < 5:
        options[choice](myIndexCards)
    else:
        print("Invalid choice. Try again.")
    # end else
# end while loop
# end
