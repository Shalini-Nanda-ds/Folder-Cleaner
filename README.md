# 🚀 Folder Cleaner Automation

🧹 **Messy folders? Not anymore!**  
This Python automation script automatically organizes files in a target folder based on their file extensions.

Think of it as your **digital housekeeper 🤖✨** that keeps your folders clean without manual effort.

---

## 🎯 What This Project Does

📂 Scans all files inside a target folder  
🔍 Detects file extensions automatically  
🗂️ Creates category folders if they don’t exist  
🚚 Moves files into their respective folders  
❓ Handles unknown extensions safely as **Others**

---

## 🧩 File Organization Logic

- 📄 `.pdf`, `.txt`, `.csv`, `.xlsx` → **Documents**
- 🖼️ `.jpg`, `.png`, `.jpeg`, `.webp` → **Images**
- 🎵 `.mp3`, `.wav`, `.ogg` → **Audio**
- 🎬 `.mp4` → **Videos**
- 📦 `.zip` → **Archives**
- ⚙️ `.exe`, `.ini` → **Executables**
- ❓ Anything else → **Others**

---

## 🛠️ Tech Stack Used

- 🐍 Python  
- 📁 `os` module – file & folder handling  
- 🚚 `shutil` module – moving files safely  

---

## ▶️ How to Run the Project

1. Clone the repository  
   ```bash
   git clone <your-repo-url>

