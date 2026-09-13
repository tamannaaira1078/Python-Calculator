#beginner python guessing game
print("===== WELCOME TO GUESSING GAME =====")
print("-"*40)
secret_number = 10
def guessing_game(secret_number):
    attempts=0
    while True:
        try:
            guess= int(input("Enter your guessed number: "))
        except ValueError:
            print("Invalid Input! Please try again.")
            continue    
        attempts+=1
        if guess>secret_number:
            print("Too High")
        elif guess<secret_number:
            print("Too Low")
        else:
            print("Congratulations!\nYou've guessed it right.") 
            print(f"It took you {attempts} attempts to guess it right.") 
            break
guessing_game(secret_number) 
print("Thanks for playing!")
print("-"*40)          

        
