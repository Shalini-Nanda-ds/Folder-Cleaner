import os
# TARGET_FILE = "C:\\Users\\Win10\\Downloads"
TARGET_FILE = r"C:\Users\Win10\Downloads"
items = os.listdir(TARGET_FILE)
for item in items:
    full_path = os.path.join(TARGET_FILE,item)

    if os.path.isfile(full_path):
        name,ext = os.path.splitext(item)
        print("FILE:",name,"-> EXTENSION:",ext)
    else:
        print("FOLDER:",item)    
