name ="vanlalawmpuia"
print(len(name))
print(name.endswith("puia"))
print(name.startswith("Van"))
print(name.capitalize())
# It is a case sencitive

# A. Changing the case of text

# text = "hello python"
# print(text.upper())       # HELLO PYTHON       
# print(text.lower())       # hello python
# print(text.title())       # Hello Python
# print(text.capitalize())  # Hello python



# B. Removing whitespace
# text = "   Hello Python   
# "print(text.strip())   # "Hello Python"
# print(text.lstrip())  # "Hello Python   "
# print(text.rstrip())  # "   Hello Python"



# C. Replacing text
# text = "I like Java"
# print(text.replace("Java", "Python"))# I like Python



# You can also specify how many replacements to make:
# text = "cat cat cat"
# print(text.replace("cat", "dog", 2))# dog dog cat



# D. Splitting and joining strings
# text = "apple,banana,orange"
# fruits = text.split(",")
# print(fruits)                                             # ['apple', 'banana', 'orange']
# result = " - ".join(fruits)print(result)                  # apple - banana - orange



# E. Finding and counting text
# text = "hello python hello"
# print(text.find("python"))  # 6
# print(text.count("hello"))  # 2
# print(text.index("python")) # 6



# Remember: find() returns -1 if the substring is not found, while index() raises a ValueError.
# F. Checking the beginning and end
# filename = "program.py"
# print(filename.startswith("program"))  # True
# print(filename.endswith(".py"))        # True



# G. Checking the contents of a string
# print("Python".isalpha())  # True
# print("12345".isdigit())  # True
# print("Python123".isalnum())  # True
# print("   ".isspace())    # True



# These methods return either True or False.
# H. Changing uppercase and lowercase
# text = "Hello PYTHON"

# print(text.swapcase())    # hELLO python