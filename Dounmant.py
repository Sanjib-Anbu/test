import os
import shutil

from_dir = "C:/Users/Computer/Downloads"
to_dir = r"C:\Users\Computer\Desktop\todir"

list_of_files = os.listdir(from_dir)

print(list_of_files)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)

    if extension.lower() == ".pdf":
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "documents_Files")
        path3 = os.path.join(path2, file_name)

        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)

    elif extension.lower() in ['.gif', '.jpg', '.jpeg', '.png', '.jfif', '.mp4']:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, "images_Files")
        path3 = os.path.join(path2, file_name)

        if os.path.exists(path2):
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
        else:
            os.mkdir(path2)
            print("Moving " + file_name + "...")
            shutil.move(path1, path3)
