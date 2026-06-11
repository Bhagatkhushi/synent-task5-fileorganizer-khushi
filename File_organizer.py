import os
import shutil
from datetime import datetime

file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"],
    "Programs": [".exe"]
}

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("❌ Invalid folder path!")
else:
    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isfile(file_path):

            moved = False

            for folder, extensions in file_types.items():

                if any(filename.lower().endswith(ext) for ext in extensions):

                    destination = os.path.join(folder_path, folder)

                    os.makedirs(destination, exist_ok=True)

                    shutil.move(
                        file_path,
                        os.path.join(destination, filename)
                    )

                    print(f"✅ {filename} moved to {folder}")

                    moved_count += 1
                    moved = True
                    break

            if not moved:

                other_folder = os.path.join(folder_path, "Others")

                os.makedirs(other_folder, exist_ok=True)

                shutil.move(
                    file_path,
                    os.path.join(other_folder, filename)
                )

                print(f"✅ {filename} moved to Others")

                moved_count += 1

    print("\n--------------------------")
    print("🎉 File Organization Completed!")
    print(f"📂 Total Files Organized: {moved_count}")
    print(f"🕒 Organized on: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
    print("--------------------------")