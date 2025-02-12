# Description: Develop a classic hangman game where the computer selects a word, and 
# the user guesses letters until they either guess the word or run out of attempts.

# Skills: Lists, strings, loops, and conditionals.
import random

def noGuess(word):
    print(f"-----------------\nSorry, you ran out of tries.\nThe correct word to guess was {word}")


def guessWord(selectedWord, correctLettersGuessed):
    while True: 
        print("\n----------------------------")
        print(f"You may now correctly spell and guess the word. \nHere are the correct letters you guessed: \n{correctLettersGuessed}")
        userGuessedWord = input("Enter the word spelled correctly: ")

        if userGuessedWord == selectedWord:
            print(f"Congratualtions you entered the correct word, which was: {selectedWord}!!!")
            break
        else:
            print("-------------------\nYou did not spell the word correctlty.")


def main():

    wordsToGuess = ["tiger", "horses","bee"]

    print("--Welcome to Hangman--\nGuess the word before you run out of attempts")

    selectedWord = random.choice(wordsToGuess)
    lengthOfWord = len(selectedWord)

    print(f"The computer has selected a word. It has a length of {lengthOfWord}.\nYou have six tries to guess the word.")

    incorrectLetters = []
    CorrectLetters = []
    tries = 0

    print("---------------------")
    while tries <= 6:
        print(f"The length of the word to guess is {lengthOfWord}")

        userGuess = input("Enter a lowercase  letter from the alplhabet to guess: ").lower()

        if userGuess in selectedWord:
            CorrectLetters.append(userGuess)
        else:
            incorrectLetters.append(userGuess)
            tries = tries+1

        
        if len(CorrectLetters) == lengthOfWord:
            guessWord(selectedWord,CorrectLetters)
            break

        if tries == 6:
            noGuess(selectedWord)
            break

        print(f"\nCorrect letters guessed: {CorrectLetters}")
        print(f"Incorrect letters guessed: {incorrectLetters}")
        print(f"Number of tries: {tries}/6")

                
main()





        



