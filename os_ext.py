#   
import os 
home_dir_path = os.path.expanduser('~')
loc =  f'{home_dir_path}/Downloads' 

# print('current directory ',os.curdir)
# print('parent directory ',os.pardir)
# print('get current working directory',os.getcwd())
# print('home directory of current user (~) : ',os.path.expanduser('~'))


# for file in os.listdir(loc):
#     print(f'file : {file}')

# print('os.path is ',os.path)

for file in os.listdir(loc):
    if '.' in file and file.rsplit('.',1)[1]=='txt':
        print(file)