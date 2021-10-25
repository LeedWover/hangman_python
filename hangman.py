word = "marketplace"

def play(word, lives):
    
    wordArray = []
    wordPlaceHolderArray = []
    sumOfGuessedLetters = 0

    for i in word:
        wordArray.append(i)
        wordPlaceHolderArray.append("_")

    while sumOfGuessedLetters < len(wordArray):
        guessedLetter = input("Guess a letter")
        for i in word:
            if(guessedLetter == i):
                
                print('You guessed it')
                print(wordPlaceHolderArray)
            else:
                print('No match')
        

play(word, 5)