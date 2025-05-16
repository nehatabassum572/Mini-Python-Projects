#THE COMPUTER HAS A RANDOM NUMBER & USER IS GUESSING 
import random;

def user_guess(x):
    random_no= random.randint(1,x)
    guess= 0;
    while guess != random_no:
        guess= int(input("Enter your guess:"))
        if guess<random_no:
            print("Oops! Too low. Try again.")
        elif guess>random_no:
            print("Oops! Too high. Try again.")
    print("Yay!! congrats, you've guessed correctly")
    
#user_guess(15)


#THE USER HAS A RANDOM NUMBER AND COMPUTER IS GUESSING
def computer_guess(x):
    low=1
    high= x
    feedback=''
    while feedback != 'c':
        
        if low!=high:
            random_no= random.randint(low, high) #THE CMP IS GENERATING RANDOM NO AS THE GUESS
        else:
            random_no= low
        feedback= input(f"Is the number {random_no} too high (H) or too low (L) or guessed correctly (C)? ").lower()
      
        if feedback=='H':
            high= random_no-1
        elif feedback=='L':
            low=random_no+1
            
    print("Yay!! The computer has guessed {random_no} correctly")
    
computer_guess(10)