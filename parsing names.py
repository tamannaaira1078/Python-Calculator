import csv
with open("students.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    names = []
    for line in csv_reader:
        name = line['name']
        names.append(name)
    html_output = "<h1>Student List</h1>"  
    html_output+="\n<u1>"  
    for name in names:
        html_output += f"\n<li>{name}</li>"
    html_output+="\n</u1>"   
    with open("student report.html", "w")  as k:
        k.write(html_output)