import os
import shutil

folder_path = input("Enter the folder path you want to organize: ")

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)

    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()

        for folder_name, extensions in file_types.items():
            if file_extension in extensions:
                new_folder_path = os.path.join(folder_path, folder_name)

                if not os.path.exists(new_folder_path):
                    os.mkdir(new_folder_path)

                new_file_path = os.path.join(new_folder_path, filename)
                shutil.move(file_path, new_file_path)

                print(f"Moved {filename} to {folder_name}")
                break

print("File organization complete.")