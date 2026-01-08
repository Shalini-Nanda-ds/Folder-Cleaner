import os
import shutil
# TARGET_FILE = "C:\\Users\\Win10\\Downloads"
TARGET_FOLDER = r"C:\Users\Win10\Downloads"
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

        print(item,"->",folder_name)       

        # shutil.move(
        #     source_path,
        #     os.path.join(destination_folder,item)
        # )    

        # print(item,"->",folder_name)
