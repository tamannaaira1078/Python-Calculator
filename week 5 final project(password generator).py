import random
import string
print("===== PASSWORD GENERATOR =====")
def get_password_length(): #asks for password length and handle invalid numbers, length 

    while True:
        try:
            pass_length = int(input("Enter Password Length: "))

        except ValueError:
            print("Invalid Input. Try Again.")
            continue
        if pass_length>=3:
            break
        else:
            print("Invalid Input! Enter a minimum input of 3.")
    return pass_length

def get_symbol_choice(): #asks whether symbols should be included and return the valid choice
    
    while True:
        choice = input("Include Symbols?(yes/no): ").strip().lower()
        if choice == "yes":
           return choice
           
           
        elif choice == "no":
           return choice
           
        else:
            print("Invalid Choice. Input yes or no.")


  
def generate_password(length, include_symbols): #create character sets and return the finished passsword
    
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    if include_symbols=="yes":
        combine= letters+numbers+symbols   
        pass_list= [random.choice(letters)]+[random.choice(numbers)]+[random.choice(symbols)] + random.choices(combine, k=length-3)
    else:
        combine = letters+numbers
        pass_list = [random.choice(letters)] + [random.choice(numbers)]+ random.choices(combine, k=length-2)
    random.shuffle(pass_list)
    password = "".join(pass_list)
    return password
pass_length = get_password_length() 
choice = get_symbol_choice()    
password = generate_password(pass_length, choice)


print(f"Your Generated Password: {password}")