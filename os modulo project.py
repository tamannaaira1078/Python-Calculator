txt_file = []
import os
print("TXT FILE REPORT")
print("-"*40)
for file in os.listdir():
    if file.endswith(".txt"):
        txt_file.append(file)
total = len(txt_file)   
for num, file in enumerate(txt_file, start=1):
    print(f"{num}.{file}")   