import random

def play():
    user = input("What is your  ? 'r'  for rock, 'p' for paper, 's' for scissors\n")
    computer  =  random.choice(['r', 'p', 's'])

    if user ==  computer:
        return 'IT\'s tie'

    # r > s, s>p  , p>r

    if is_win(user, computer):
        return 'You won !'
    
    return 'You lost !'

def is_win(player, opponent):
    #return true if user win
    # r > s, s>p  , p>r

    if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    
print (play())