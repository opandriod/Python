a =31
t = type (a) #class<int>
print(t)

b="31"
t = type (b) #class<str>
print(t)

# Everything inside "" is a string. It can be a number, a word, or a sentence. It is always treated as a string.

x=31
t=float(x) #class<float>
print(t)

a="31"
b = float(a) #class<float>
t=type(b)
print(t)
# type() is a built-in function that returns the type of the object passed to it. 
# It can be used to check the type of any object in Python.