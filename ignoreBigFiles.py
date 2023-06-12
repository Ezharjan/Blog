import os

# 获取当前目录
# current_dir = os.getcwd() # Linux OS
current_dir = os.getcwd().replace("\\", "/") # Windows OS

# 遍历当前文件夹下所有文件和文件夹，并记录文件名超过49.99MB的文件
ignore_list = []
for foldername, subfolders, filenames in os.walk(current_dir):
    for filename in filenames:
        file_path = os.path.join(foldername, filename)
        if os.path.getsize(file_path) > (49.99 * 1024 * 1024):
            # ignore_list.append(file_path[len(current_dir)+1:]) # Linux OS
            ignore_list.append(file_path[len(current_dir)+1:].replace("\\", "/")) # Windows OS

# 将记录的文件名添加到.gitignore文件中
gitignore_path = os.path.join(current_dir, ".gitignore")
if not os.path.isfile(gitignore_path):
    with open(gitignore_path, 'w') as f:
        pass
with open(gitignore_path, 'a') as f:
    for item in ignore_list:
        f.write(item + '\n')
