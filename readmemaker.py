import os

currentdir = os.path.dirname(os.path.realpath(__file__))
file_list = os.listdir(currentdir)
folder_list = [x for x in file_list if "." not in x]


readme = open(os.path.join(currentdir,'README.md'), 'w+')

readme.write("# Tim's Textbooks\n")
readme.write("## 📝 Here are my textbooks by class, updated whenever\n")
readme.write("If any questions, DM me on Discord (grampachampa) and I'll answer!\n")
readme.write("## ✍🏻 Table of contents\n")

for folder in folder_list:
    readme.write(f"### {folder}\n")
    files = os.listdir(os.path.join(currentdir, folder))
    counter = 0
    for file in files:
        counter +=1
        readme.write(f"{counter}) {file}\n")
    readme.close()

