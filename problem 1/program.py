import os

# tells the path of the directory you want to list
directory = "/"

# now the program will list all the files and directories in the specified path
contents = os.listdir(directory)

# now the program will print all the files and directories in the specifies path
for item in contents:
    print(item)