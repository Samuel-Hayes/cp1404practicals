import os
import shutil

file_types = [".txt", ".xls", ".xlsx", ".png", ".jpg", ".gif", ".doc", ".docx"]
os.chdir('FilesToSort')

for filename in os.listdir('.'):
    for file_type in file_types:
        if filename.endswith(file_type):
            if not os.path.exists(file_type.replace('.', '')):
                os.mkdir(file_type.replace('.', ''))
            shutil.move(filename, file_type.replace('.', ''))
