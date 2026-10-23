# 1. count()
# Counts how many times a value appears in a tuple.
numbers = (10, 20, 10, 30, 10)
print(numbers.count(10))

# Output:3

# 2. index()
# Returns the index (position) of the first occurrence of a value.
fruits = ("apple", "banana", "mango", "banana")
print(fruits.index("banana"))



# Output:1


# Remember: Python indexing starts from 0.
# 2. Other useful tuple operations
# These are not tuple methods, but they are commonly used when working with tuples.
# Operation     	Example	                    Result
# len()	        len((1, 2, 3))	                   3
# max()	        max((10, 20, 5))	               20
# min()	        min((10, 20, 5))	               5
# sum()	        sum((1, 2, 3))	                   6
# sorted()	    sorted((3, 1, 2))	            [1, 2, 3]
# in	        2 in (1, 2, 3)	                   True
# len()	        len(())	                           0

# 3. Why does a tuple have only two methods?
# Tuples are immutable, so you cannot use methods like append(), remove(), or sort() directly on them.
numbers = (1, 2, 3)
# These will cause errors:# numbers.append(4)# numbers.remove(2)# numbers.sort()



# If you need to modify a tuple, you can convert it to a list first:
numbers = (3, 1, 2)
my_list = list(numbers)
my_list.append(4)
my_list.sort()
numbers = tuple(my_list)
print(numbers)



# Output:
# (1, 2, 3, 4)


# For your Python studies, remember: The two official tuple methods are count() and index()