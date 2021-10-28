import os
from word_exproter import *
from graphic_engine import listPrint
from graphics import *


def collector():
    menu_starter(menu)
    listPrint(difficulty)
    import_print("./talk_test.txt")
    inputResult = input('\nKowalsky: Készen állsz?[Y/N]').lower()
    if(inputResult.lower() == 'n'):
        quit() 
    dif = selectDifficulty()
    live = lives(dif)
    word = exporter(dif)
    
    print("".join(word.split(" ")))
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
        #if i != " ":
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
               
            if wordArray == wordPlaceHolderArray:
                import_print("./win.txt")
                os.system('cls' if os.name == 'nt' else 'clear')
                import_print("./credit_scene.txt")
                inputResult = input('\nKowalsky: Megpróbálod újra?[Y/N]').lower()
                if inputResult.lower() == 'n':
                    print('Goodbye')
                    quit() 
                elif inputResult.lower() == 'y':
                    collector()  
                

        print(guessedLetter)       
        if (founds <= 0):
            if lives == 2:
                import_print("./beszolas.txt")
            print(szakaszok[lives - 1])
            badGuesses.append(guessedLetter)
            os.system('cls' if os.name == 'nt' else 'clear')
            lives -= 1

        if(lives <= 0):
            listPrint(reject)
            import_print("./game_over.txt")
            os.system('cls' if os.name == 'nt' else 'clear')
            import_print("./credit_scene.txt")
            inputResult = input('\nKowalsky: Megpróbálod újra?[Y/N]').lower()
            if inputResult.lower() == 'n':
                print('Jó volt veled játszani!')
                quit() 
            elif inputResult.lower() == 'y':
                collector()  
            else: 
                quit()

          

collector()