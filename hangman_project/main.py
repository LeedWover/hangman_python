import os
from word_exproter import *
from graphic_engine import listPrint
from graphics import *


def collector():
    #menu_starter(menu)
    #listPrint(difficulty)
    dif = selectDifficulty()
    #import_print("./talk_test.txt")

    live = lives(dif)
    word = exporter(dif)
    
    print(word)
    return play(word, live)

def formatInputStr(guessedLetter, badGuesses):
    while guessedLetter == 'quit':
        quitMsg = input('Are you sure? [Y/N]').lower()
        if(quitMsg == 'y'):
            print('Goodbye')
            exit()
        elif(quitMsg == 'n'):
            print('\nThen continue the game')
            guessedLetter = input("\nGuess a letter: ").lower()
        else:
            print('\nBad format')
         
    while len(guessedLetter) > 1 or len(guessedLetter) < 1:
        guessedLetter = input('Bad format, try again: ')
    while guessedLetter.isdigit():
        guessedLetter = input('Numbers are not allowed, try again: ')
    while badGuesses.count(guessedLetter) > 0:
        guessedLetter = input('You have tried this letter, try another one: ')
    return guessedLetter

def play(word, lives):
    os.system('cls' if os.name == 'nt' else 'clear')
    wordArray = []
    badGuesses = []
    wordPlaceHolderArray = []
    wordPlaceHolder = " _ " * len(word)
    sumOfGuessedLetters = 0
    guessedLetter = ''
    for i in word:
        wordArray.append(i)
        wordPlaceHolderArray.append("_")

    while sumOfGuessedLetters < len(wordArray):
        print(badGuesses)
        print(word)
        i = 0
        founds = 0
        print(szakaszok[::-1][lives].format( '♥ ' * lives, wordPlaceHolder))
        print(badGuesses)
        #os.system('cls' if os.name == 'nt' else 'clear')
        
        guessedLetter = formatInputStr(input("\nGuess a letter: ").lower(), badGuesses)
        for letter in wordArray:
            i += 1
            if(letter.lower() == guessedLetter):
                wordPlaceHolderArray[i - 1] = letter
                wordPlaceHolder = "  ".join(wordPlaceHolderArray)
                sumOfGuessedLetters += 1
                founds += 1
                os.system('cls' if os.name == 'nt' else 'clear')
               
            elif wordArray == wordPlaceHolderArray:
                print(f"\n\nYou got it!\n\nThe invented word is:\n\n{word}")
        print(guessedLetter)       
        if (founds <= 0):
            print('No match')
            print(szakaszok[lives - 1])
            badGuesses.append(guessedLetter)
            os.system('cls' if os.name == 'nt' else 'clear')
            lives -= 1

        if(lives <= 0):
            print(f'You lost!\nThe invented word was:\n\n{word}')

            return 
        

collector()