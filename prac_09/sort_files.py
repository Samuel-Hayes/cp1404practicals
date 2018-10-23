import os
import shutil

file_types = {".txt": '', ".xls": '', ".xlsx": '', ".png": '', ".jpg": '', ".gif": '', ".doc": '', ".docx": ''}
categories = []
os.chdir('FilesToSort')

for filename in os.listdir('.'):
    for file_type in file_types:
        if filename.endswith(file_type):
            if not os.path.exists(file_type.replace('.', '')):
                os.mkdir(file_type.replace('.', ''))
            shutil.move(filename, file_type.replace('.', ''))

# for file_type in file_types:
#     category = str(input("What category would you like to sort {} files into".format(file_type)))
#     categories.append(category)
#     file_types[file_type] = category
#     if not os.path.exists(category):
#         os.mkdir(category)
#
# for filename in os.listdir('.'):
#     for file_type in file_types:
#         if filename.endswith(file_type):
#             shutil.move(filename, file_types[file_type])

