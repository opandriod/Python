#Write a program to detect double space in a string

a = "This    is a string"

print(a.find("  "))
#If the output is -1 that means there is no double spaces 

print(a.find("string"))
#It is counted in an index so in this condition the output will be 13