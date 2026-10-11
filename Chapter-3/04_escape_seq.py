print("Hello,\n Vanlalawmpuia hope you doing great and achieved some of your dreams")

a = ("Vanlalawmpuia is also called \"opa\"")
b = ('\nVanlalawmpuia is also called \'opa\'')
print(a,b)

# Examples with Python code
# A. New line (\n)
# print("Hello\nWorld")



# Output: Hello World

# B. Tab (\t)
# print("Name:\tJohn")
# print("Age:\t21")

# Output: Name:   John Age:    21


# The spacing is a tab, so the exact alignment depends on the display.
# C. Printing quotation marks
# print("He said, \"Hello!\"")
# print('It\'s a beautiful day')



# Output:
# He said, "Hello!"
# It's a beautiful day


# D. Printing a backslash (\\)
# print("C:\\Users\\Python")



# Output:
# C:\Users\Python


# E. Unicode characters
# print("\u2764")       # ❤️ (heart symbol)
# print("\U0001F600")   # 😀print("\x41")        
#  # Aprint("\101")         # A



# 3. Important: Raw strings (r"")
# A raw string treats most backslashes as literal characters instead of interpreting them as escape sequences.
# print(r"Hello\nWorld")



# Output:
# Hello\nWorld


# This is especially useful for Windows file paths and regular expressions.
# path = r"C:\Users\Student\Documents"
# print(path)



# Output:
# C:\Users\Student\Documents


# Note: Raw strings have some restrictions; for example, a raw string cannot end with an odd number of backslashes, such as r"hello\".
# 4. Quick practice
# Try predicting the output before running this code.
# print("Python\nProgramming")
# print("Python\tProgramming")
# print("I am learning \"Python\"")
# print("A\\B\\C")
# print("Hello\bWorld")
