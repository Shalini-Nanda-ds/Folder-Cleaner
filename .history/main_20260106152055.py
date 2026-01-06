import os
# TARGET_FILE = "C:\\Users\\Win10\\Downloads"
TARGET_FILE = r"C:\Users\Win10\Downloads"
items = os.listdir(TARGET_FILE)
extension_count = {}
for item in items:
    full_path = os.path.join(TARGET_FILE,item)

    if os.path.isfile(full_path):
        name,ext = os.path.splitext(item)
        # print("FILE:",name,"-> EXTENSION:",ext)
        if ext in extension_count:
            extension_count[ext] += 1
        else:
            extension_count[ext] = 1    
    else:
        print("FOLDER:",item)  

print("\nExtension Summary")
for ext,count in extension_count.items():
    print(ext,":",count)          
