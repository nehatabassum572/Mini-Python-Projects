import random

def play():
    user_choice= input("What's your choice?\n 1.'r' for rock \n 2.'p' for paper \n 3.'s' for scissor\n")
    comp_choice= random.choice(['r','p','s'])
    
    if user_choice==comp_choice:
        return 'Its a tie!'
    if is_win(user_choice, comp_choice):
        return 'You win!'
        
    return 'You lost!'
        
    
def is_win (player, opponent):
    #r>s, p>s, s>p
    
    if (player=='r' and opponent=='s') or (player=='p' and opponent=='s') or\
        (player=='s' and opponent=='p'):
        return True
    
    
print(play())