import os
print("FILE REPORT")
print("-"*40)
for file in os.listdir():
    byte_size = os.stat(file).st_size
  
    if byte_size>100:
        print(f"{file:<40}{byte_size:>10}")



    


