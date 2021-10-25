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
        guessedLetter = input("Guess a letter")
        for letter in wordArray:
            i += 1
            print(letter)
            if(letter == guessedLetter):
                print('You got it')
                wordPlaceHolderArray[i - 1] = letter
                sumOfGuessedLetters += 1
            else:
                print('No match')
            print(wordPlaceHolderArray)   
    

play(word, 5)
