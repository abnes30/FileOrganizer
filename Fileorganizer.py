import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def organize_files(directory):
    if not os.path.exists(directory):
        print("Error: Directory does not exist!")
        return
    
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):  # Ignore directories
            file_extension = os.path.splitext(filename)[1].lower()
            
            # Find the matching category
            folder_name = "Others"
            for category, extensions in FILE_CATEGORIES.items():
                if file_extension in extensions:
                    folder_name = category
                    break
            
            folder_path = os.path.join(directory, folder_name)
            os.makedirs(folder_path, exist_ok=True)
            
            shutil.move(filepath, os.path.join(folder_path, filename))
            print(f"Moved {filename} → {folder_name}/")

if __name__ == "__main__":
    target_directory = input("Enter the directory to organize: ")
    organize_files(target_directory)
