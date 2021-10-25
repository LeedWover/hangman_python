word = "marketplace"


def play(word, lives):
    szakaszok = [
            """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                    """,

            """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                    """,

            """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |      
                    -
                    """,

            """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                    """,

            """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                    """,

            """
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                    """,

            """
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                    """
    ]
    import msvcrt
    import os
    import time
    wordArray = []
    wordPlaceHolderArray = []
    charNotFound = []
    sumOfGuessedLetters = 0
    for i in word:
        wordArray.append(i)
        wordPlaceHolderArray.append("_ ")

    while sumOfGuessedLetters < len(wordArray):

        os.system('cls')
        i = 0
        founds = 0
        print(szakaszok[lives -1])
        print(wordPlaceHolderArray)
        print('lives', lives)
        print(charNotFound)
        guessedLetter = input("Guess a letter: ")
        if(len(guessedLetter) > 1):
            guessedLetter = input("Bad formatted input, guess only one letter")
        for letter in wordArray:
            i += 1
            if(letter == guessedLetter):
                wordPlaceHolderArray[i - 1] = letter
                sumOfGuessedLetters += 1
                founds += 1
        if (founds <= 0):
            lives -= 1
            charNotFound.append(guessedLetter)
        if(lives <= 0):
            print('You lost')
            return

play(word, 7)
