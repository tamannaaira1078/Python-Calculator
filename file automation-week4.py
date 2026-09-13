#this project is about changing the file name
#first we have to import os
import os
#we have to put all the file here with listdir
for file in os.listdir():
    if file.endswith(".txt"):
        file_name, file_ext = os.path.splitext(file)  #basically we are spliting the file into name and extension
        print("Full file:", file)
        print("File Name:", file_name)
        print("Extension:", file_ext)
        print("-"*30)
    #now we have to break the file name into title, course and number
        title, course, number = file_name.split("-")
        title = title.strip()
        course = course.strip()
        number = number.strip()[1:].zfill(2) #using strip function for removing unnecessary space
        #used slicing for removing hastag and used zfill for number sorting
        print("Title:", title)
        print("Course:", course)
        print("Number:", number)
        print("-"*30)
    #now we have to rename our file with os.rename
        new_name = f"{number}-{title}{file_ext}"
        os.rename(file, new_name)

