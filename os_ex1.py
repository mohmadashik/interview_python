import os
import datetime

q='Exercise 1: Current Working Directory'
print(q)
# Print the current working directory.
print(f'current working directory ',os.getcwd())

q = 'Exercise 2: List Files'
print(q)
# List all files in the current directory.
for file in os.listdir(os.getcwd()):
    print(f'file : {file}')


# q='Exercise 3: Create Directory'
# print(q)
# # Create a new directory named "exercise_dir" in the current directory.
# new_dir = 'new_directory3'
# result = os.mkdir(new_dir)
# print('mkdir return result ',result)



# q='Exercise 4: File Existence'
# print(q)

# # Check if a file named "example.txt" exists in the current directory.
# print('create directory worked or not? ',new_dir in os.listdir(os.getcwd()))

q='Exercise 5: File Information'
print(q)

# Get information about a file, such as size, creation time, and modification time.
# file_name = 'multithreading.py'
# file_info = os.stat(file_name)
# print('file size :',file_info.st_size,' bytes')
# print('file created time: ',datetime.datetime.fromtimestamp(file_info.st_ctime))
# print('file modified time: ',datetime.datetime.fromtimestamp(file_info.st_mtime))

# q='Exercise 6: Rename File'
# print(q)
# os.rename(file_name,'multithreading-ex.py')
# print(os.listdir())

# Rename the file "old_name.txt" to "new_name.txt".

# q='Exercise 7: Delete Directory'
# print(q)
# print(os.listdir())
# os.rmdir('new_directory')
# print(os.listdir())

# Delete the directory "exercise_dir" created earlier.

q='Exercise 8: List Subdirectories'
print(q)

#List all subdirectories in the current directory
dir_path = os.path.expanduser('~')+'/Downloads'
print(dir_path)
subs_download = [dir for dir in os.listdir()if os.path.isdir(dir)]
print(subs_download)
# print(os.listdir(dir_path))

q='Exercise 9: File Extension'
print(q)

for file in os.listdir():
    if '.' in file :
        print(f' file {file}  and extension is {file.rsplit(".",1)[1]}')

# Get the file extension of all files in the current directory.

q='Exercise 10: Recursive File List'
print(q)

# List all files in the current directory and its subdirectories recursively.
import os

def list_files_recursive(directory=dir_path):
    for root, dirs, files in os.walk(directory):
        for file in files:
            print(os.path.join(root, file))

print(os.walk(dir_path))

# list_files_recursive()
# git@github.com-mohmadashik:mohmadashik/interview_python.git