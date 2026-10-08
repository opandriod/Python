# Write a python program to print the contents of a directory using the OS module.
# search online for the function which does that and use it in your program.    

import os

# Specify the directory
path = "."

# Get the contents of the directory
contents = os.listdir(path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)