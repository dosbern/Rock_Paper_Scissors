import random, sys
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
round = 1
computerMove = None
print(' ')
input('Press enter to begin')
for x in range(1, 31):
    print(' ')
while True:
    print(' ')
    while True:
        print('Choose your Move:')
        print('(R)ock, (P)aper, (S)cissors or (Q)uit')
        playerMove = input()
        playerMove = playerMove.lower()
        #playerMove = str(playerMove)
        if playerMove == 'q':
            sys.exit()
        elif playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        else:
            print('Invalid Selection')
            continue
    print(' ')
    computerChoice = random.randint(1, 3)
    if computerChoice == 1:
        computerMove = 'r'
    if computerChoice == 2:
        computerMove = 'p'
    if computerChoice == 3:
        computerMove = 's'
    #battle begins
    if playerMove == 'r':
        print('________________________________________')
        print('____________________Round: ' + str(round) +'____________')
        print(' ')
        print('Rock vs...')
    if playerMove == 'p':
        print('________________________________________')
        print('____________________Round: ' + str(round) +'____________')
        print(' ')
        print('Paper vs...')
    if playerMove == 's':
        print('________________________________________')
        print('____________________Round: ' + str(round) +'____________')
        print(' ')
        print('Scissors vs...')
    if computerMove == 'r':
        print('Rock')
    if computerMove == 'p':
        print('Paper')
    if computerMove == 's':
        print('Scissors')
        #ties
    if playerMove == computerMove:
        ties = ties + 1
        print(' ')
        print('It was a tie!')
        round = round + 1
        #wins
    if playerMove == 'r' and computerMove == 's':
        wins = wins + 1
        print(' ')
        print('You won!')
        round = round + 1
        print(' ')
    if playerMove == 'p' and computerMove == 'r':
        wins = wins + 1
        print(' ')
        print('You won!')
        round = round + 1
        print(' ')
    if playerMove == 's' and computerMove == 'p':
        wins = wins + 1
        print(' ')
        print('You won!')
        round = round + 1
        print(' ')
        #losses
    if playerMove == 'r' and computerMove == 'p':
        losses = losses + 1
        print(' ')
        print('You lost!')
        rouns = round + 1
        print(' ')
    if playerMove == 'p' and computerMove == 's':
        losses = losses + 1
        print(' ')
        print('You lost!')
        round = round + 1
        print(' ')
    if playerMove == 's' and computerMove == 'r':
        losses = losses + 1
        print(' ')
        print('You lost!')
        round = round + 1
        print(' ')
    #score
    print(' ')
    print('Your score:')
    print('Wins: ' + str(wins))
    print('Losses: ' + str(losses))
    print('Ties: ' + str(ties))
    #wait to clear
    print('Press enter to continue...')
    input()
    for x in range(1, 31):
        print(' ')