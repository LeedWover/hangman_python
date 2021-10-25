word = "marketplace"


def play(word, lives):

    wordArray = []
    wordPlaceHolderArray = []
    sumOfGuessedLetters = 0
    for i in word:
        wordArray.append(i)
        wordPlaceHolderArray.append("_")

    while sumOfGuessedLetters < len(wordArray):
        i = 0
        founds = 0
        guessedLetter = input("Guess a letter")
        for letter in wordArray:
            i += 1
            if(letter == guessedLetter):
                print('You got it')
                wordPlaceHolderArray[i - 1] = letter
                sumOfGuessedLetters += 1
                founds += 1
        if (founds <= 0):
            print('No match')
            lives -= 1
        print('lives', lives)
        if(lives <= 0):
            print('You lost')
            return


play(word, 5)


def akasztofa(probak):
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
    return szakaszok[probak]
