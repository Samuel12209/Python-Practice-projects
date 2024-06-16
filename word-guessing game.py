from random_word import RandomWords

r = RandomWords()

ran_word = r.get_random_word().lower()

word = list(ran_word)

blank_space = list("_" * len(word))

while True:
    blank_space = "".join(blank_space)
    if blank_space == ran_word:
        print("."*10)
        print("You guessed the Word! it was", ran_word)
        exit()

    print(blank_space)
    blank_space = list(blank_space)
    
    guess = input("Guess a letter: ").lower()
    
    if guess.isalpha() and len(guess) == 1:

        if guess in ran_word:
            print("."*10)
            print("The letter: " + guess + " Was correct!")
            for i in range(len(word)):
                if word[i] == guess:
                    blank_space[i] = guess 
                    i += 1

        else:
            print("Try again")
    
    else:
        print("Please type ONE letter")