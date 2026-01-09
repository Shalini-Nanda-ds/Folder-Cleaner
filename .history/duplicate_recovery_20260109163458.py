import os
import shutil

ROOT_FOLDER = r"C:\Users\Win10\Downloads"

def clean_duplicates(folder_path):
    seen_files = set()
    duplicate_folder = os.path.join(folder_path,"_DUPLICATES")
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path,item)

        if not os.path.isfile(item_path):
            continue

        if item in seen_files:
            if not os.path.exists(duplicate_folder):
                os.makedirs(duplicate_folder)
                
            shutil.move(item_path,os.path.join(duplicate_folder,item))
            print("DUPLICATE MOVED:",item_path)    

        else:
            seen_files.add(item)
            
    for folder in os.listdir(ROOT_FOLDER):
            full_path = os.path.join(ROOT_FOLDER,folder)

            if os.path.isdir(full_path):
                clean_duplicates(full_path)

    print("\n Duplicate recovery completed safely.")                    