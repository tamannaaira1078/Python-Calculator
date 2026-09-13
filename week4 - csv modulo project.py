import csv
with open("students.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    print("STUDENT REPORT MANAGER")
    print("-"*40)
    print(f"{'Name':<20}{'Marks':<12}{'Grade':<8}")
    print("-"*40)
    def get_grades(marks):
        if marks>=90:
            grade = "A+"
        elif marks>=80:
            grade = "A"  
        elif marks >=70:
            grade = "B" 
        elif marks>=60:
            grade = "C" 
        else:
            grade = "Fail" 
        return grade 
    all_marks = []
    for line in csv_reader:
        marks = int(line['marks'])  
        grade = get_grades(marks) 
        all_marks.append(marks)
        print(f"{line['name']:<20}{marks:<12}{grade:<8}")
    print("-"*40) 
    print(f"{'Average Marks':<12}:{sum(all_marks)/len(all_marks)}")  
    print(f"{'Highest Marks':<12}:{max(all_marks)}") 
    print(f"{'Lowest Marks':<12}:{min(all_marks)}")
    print(f"{'Total Students':<12}:{len(all_marks)}")






    

                

    