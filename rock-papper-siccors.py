import random

player = 0
player2 = 0
options = ['rock','paper','sissors']

def RockPaperSissors(options, player, player2):
    print('-'*10)
    choice = input('Choose Rock, paper or sissors: ').lower()
    bot = random.choice(options)
    if choice == 'rock':
        if bot == 'paper':
            player2 += 1
            print('Bot chose: ',bot)
        else:
            player += 1
    elif choice == 'paper':
        if bot == 'sissors':
            player2 += 1
            print('Bot chose: ',bot)
        else:
            player += 1
    elif choice == 'sissors':
        if bot == 'rock':
            player2 += 1
            print('Bot chose: ',bot)
        else:
            player += 1
    else:
        print('Please choose Rock, paper or sissors')
        RockPaperSissors(options, player, player2)

    print('-'*10)
    print('You have ',player, ' points')
    print('bot has',player2, ' Points')

while True:
    RockPaperSissors(options, player, player2)
