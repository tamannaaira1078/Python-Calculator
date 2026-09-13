import csv
while True:
    print("===== CONTACT MANAGER =====")
    print("1. Show Contacts \n2. Add Contact \n3. Search Contact \n4. Exit")
    choice = int(input("Choose an option(1/2/3/4): "))
    if choice == 1:
        print("**You Chose Show Contact**")
        with open("contacts.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            print(f"{'Name':<20}{'Phone':<12}{'Email':<35}") 
            print("-"*60)
            for line in csv_reader:
                 print(f"{line['name']:<20}{line['phone']:<12}{line['email']:<35}")
    elif choice == 2:
        print("**You Chose Add Contact**") 
        name = input("Enter Name: ")  
        phone = input("Enter Phone: ")
        email = input("Enter Email: ")
        with open("contacts.csv", "a", newline="") as csv_file:
            fields = ["Name", "Phone", "Email"]
            csv_writer = csv.DictWriter(csv_file, fieldnames = fields)
            csv_writer.writerow({"Name": name, "Phone": phone, "Email": email})
            print("Contact Svaed Successfully!!")
        

    elif choice == 3:
        print("**You chose Search Contact**")  
        name = input("Enter Contact Name: ").strip().lower()
        with open("contacts.csv", "r") as csv_file:
            csv_reader =csv.DictReader(csv_file)
            found = False
            for line in csv_reader:
                if name == line['name']:
                    found = True
                    print(f"{'Name':<12}:{line['name']}")
                    print(f"{'Phone':<12}:{line['phone']}")
                    print(f"{'Email':<12}:{line['email']}")
            if not found:
                print("Contact Not Found")  




    elif choice ==4:
        print("**You chose Exit**") 
        break
    else:
        print("Invalid Choice!1")  

