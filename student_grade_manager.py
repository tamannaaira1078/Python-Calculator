students = []
while True:
    try:
        numbers= int(input("How many Students?" ))
        if numbers>0:
                break
        else:
            print("Please enter atleast 1 student.")
        
    except ValueError:
        print("Invalid Input.Please try again.") 
       
for num in range(1, numbers+1):
    name = input(f"Enter student{num} name: ")
    while True:
        try:
            marks = int(input(f"Enter student{num} marks: "))
            if 0<=marks<=100:
                break
            else:
                print("Marks must be between 0 and 100")
            
        except ValueError:
            print("Invalid Input. Please try again.")
            

    students.append((name, marks))
students.sort(key=lambda s:s[1], reverse=True) 
print("STUDENT GRADE MANAGER")  
print("-"*40)
print(f"{'Name':<20}{'Marks':<10}{'Grade':<8}") 
print("-"*40) 
def get_grade(marks):
    if marks>=90:
        grade="A+"  
    elif marks>=80:
        grade="A"  
    elif marks>=70:
        grade="B" 
    elif marks>=60:
        grade="C"
    else:
        grade="Fail" 
    return grade
for name, marks in students:
    grade= get_grade(marks)
    print(f"{name:<20}{marks:<10}{grade:<8}")
print("-"*40)
all_marks = [marks for name, marks in students]
print(f"{'Average Marks'}:{sum(all_marks)/len(all_marks)}")
print(f"{'Highest Marks'}:{max(all_marks)}")
print(f"{'Lowest Marks'}:{min(all_marks)}") 
print(f"{'Total Students'}:{len(all_marks)}")   



