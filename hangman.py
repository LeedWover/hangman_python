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
    import os
    wordArray = []
    wordPlaceHolderArray = []
    sumOfGuessedLetters = 0
    for i in word:
        wordArray.append(i)
        wordPlaceHolderArray.append("_")

    while sumOfGuessedLetters < len(wordArray):

        i = 0
        founds = 0
        guessedLetter = input("Guess a letter: ")
        os.system('cls')
        if(len(guessedLetter) > 1):
            guessedLetter = input("bad formatted input, guess only one letter")
        for letter in wordArray:
            i += 1
            if(letter == guessedLetter):
                print('You got it')
                wordPlaceHolderArray[i - 1] = letter
                sumOfGuessedLetters += 1
                founds += 1
                print(wordPlaceHolderArray)
        if (founds <= 0):
            print('No match')
            print(szakaszok[lives - 1])
            lives -= 1
        print('lives', lives)
        if(lives <= 0):
            print('You lost')
            return


play(word, 7)
