import os
import shutil
# TARGET_FILE = "C:\\Users\\Win10\\Downloads"
TARGET_FOLDER = r"C:\Users\Win10\Downloads"
TEST_MODE = True
EXTENSION_MAP = { 
    # Documents
    ".pdf" : "Documents",
    ".txt" : "Documents",
    ".csv" : "Documents",
    ".xlsx" : "Documents",
    ".pbix" : "Documents",
    ".ipynb" : "Documents",

    #Images

    ".jpg" : "Images",
    ".png" : "Images",
    ".jpeg" : "Images",
    ".webp" : "Images",

    # Videos
    ".mp4" : "Videos",
    
    # Audio
    ".mp3" : "Audio",
    ".wav" : "Audio",
    ".ogg" : "Audio",

    # Archives
    ".zip" : "Archives",

    # System / Executables
    ".exe" : "System",
    ".ini" : "System",
    ".winmd" : "System",

}
# Summary Counters

moved_count = 0
skipped_count = 0
category_count = {}

# Main Logic
items = os.listdir(TARGET_FOLDER)
# extension_count = {}
for item in items:
    source_path = os.path.join(TARGET_FOLDER,item)

    if item in EXTENSION_MAP.values():
        continue

    if os.path.isfile(source_path):
        _,ext = os.path.splitext(item)
        # print("FILE:",name,"-> EXTENSION:",ext)
        ext = ext.lower()
        
        folder_name = EXTENSION_MAP.get(ext,"Others")
        destination_folder = os.path.join(TARGET_FOLDER,folder_name)

        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
            
        destination_path = os.path.join(destination_folder,item)

        # Duplicate file check 
        if os.path.exists(destination_path):
            print("SKIPPED (already exists):",item)
            skipped_count += 1
            continue   
        
        # Summary Count
        category_count[folder_name] = category_count.get(folder_name,0) + 1

        if TEST_MODE:
            print("[TEST MODE]",item,"->",folder_name)
        else:
            shutil.move(source_path,destination_path)
            print("[MOVED]",item,"->",folder_name)
            moved_count += 1

# Final Summary 
print("\n===== SUMMARY ======")
print("Mode:","TEST MODE" if TEST_MODE else "REAL MODE")
print("Files moved:",moved_count)
print("Files skipped:",skipped_count)

for category,count in category_count.items():
    print(f"{category}: {count} file(s)")
   

      
