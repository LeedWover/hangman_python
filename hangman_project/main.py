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


def play(word, lives):
    os.system('cls' if os.name == 'nt' else 'clear')
    wordArray = []
    badGuesses = []
    wordPlaceHolderArray = []
    wordPlaceHolder = " _ " * len(word)
    sumOfGuessedLetters = 0
    for i in word:
        wordArray.append(i)
        wordPlaceHolderArray.append("_")

    while sumOfGuessedLetters < len(wordArray):
        i = 0
        founds = 0
        print(szakaszok[::-1][lives].format(
              '♥ ' * lives,  wordPlaceHolder, badGuesses ))
        guessedLetter = input("\nGuess a letter: ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')
        if(len(guessedLetter) > 1):
            guessedLetter = input("bad formatted input, guess only one letter")
        for i in badGuesses:    
            if(guessedLetter == i):
                guessedLetter = input("this letter already guessed")
            guessedLetter = input("bad formatted input, guess only one letter")
        for letter in wordArray:
            i += 1
            if(letter.lower() == guessedLetter):
                wordPlaceHolderArray[i - 1] = letter
                wordPlaceHolder = "  ".join(wordPlaceHolderArray)
                sumOfGuessedLetters += 1
                founds += 1
               
            elif wordArray == wordPlaceHolderArray:
                print(f"\n\nYou got it!\n\nThe invented word is:\n\n{word}")
                
        
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