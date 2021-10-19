 #!/usr/bin/python

"""
Python  Functions
"""


# Write a Python function unique_list() that takes a list and returns a new list with unique elements of the first list.
# unique_list: (1,2,3,3,3,3,4,4,5)

def unique_list(args):
	x = []
	for i in args:
		if i not in x:
			x.append(i)
	return x


#Write a Python function multiply()to multiply all giving numbers in a list.
#Sample List : (9, 2, 3, -6, 7)
#Expected Output : -2268

 
def multiply(args):
	total = 1
	for i in args:
		total *= i

	return total
# Write a function get_average() that takes an arbitrary number of arguments and returns the average of them
# Number of arguments : (5,6,8,10,31)
# Expected Output : 12

def get_average(*args):
	num = 0
	count = len(args)
	for i in args:
		num += i
	return num/count
