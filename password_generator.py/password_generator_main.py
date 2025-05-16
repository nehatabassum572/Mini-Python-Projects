import random 
import string 

def generate_pwd(min_length, number=True, special=True):
    letter= string.ascii_letters
    digit= string.digits
    special_char= string.punctuation

    charecter = letter
    if number:
        charecter += digit
    if special:
        charecter += special_char
    
    pwd= []
    has_number= False
    has_special= False 
    while len(pwd) < min_length or not (has_number or not number) or not (has_special or not special):
        new_char = random.choice(charecter)
        pwd.append(new_char)
        if new_char in digit:
            has_number = True
        if new_char in special_char:
            has_special = True

    random.shuffle(pwd)  # Shuffle to avoid predictable patterns
    return "".join(pwd[:min_length])  # Ensure exact length



min_length= int(input("Enter the Minimum length of the password:"))
has_number= input("Do you want the password to have Numbers? (yes/no)").lower() == "yes"
has_special= input("Do you want the password to have Special Charecters? (yes/no)").lower() == "yes"
generated_pwd= generate_pwd(min_length, has_number, has_special)
print("The generated password is:", generated_pwd)