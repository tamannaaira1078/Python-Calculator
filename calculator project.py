#This function calculates the numbers with preferred operator and returns result
def calculator(num_1, num_2, operator):   
        if operator=="+":
            return num_1 +num_2
        elif operator=="-":
            return num_1 - num_2  
        elif operator =="*":
            return num_1*num_2  
        elif operator =="/":
            if num_2==0: 
                return "Error!Cannot accept number less than 1."
            return num_1/num_2
        
    
while True: 
    print("===== Python Calculator =====")
    user_choice =input("Do you want to continue?(yes/no): ").strip().lower() # asking the user choice first for smoother experience
    if user_choice=="yes":
        pass
    elif user_choice=="no":
        print("Goodbye!")
        break
    else:
        print("Invalid Input.Please type yes or no.") 
        continue
    operator = input("Enter Preferred Operator(+,-,/,*): ")
    if operator not in ["+", "-", "/", "*"]: 
        print("Invalid Operator. Please try again.")
        continue
    try:
        num_1 = int(input("Enter Your First Number: "))
        num_2 = int(input("Enter Your Second Number: "))
        
    except ValueError:
        print("Invalid Input!") 
        continue
    
    result = calculator(num_1, num_2, operator) #using the function in result variable
    print(f"{'Result'}:{result}")
        


   