# python 2

def colatz(n):
	if n%2 == 0:
		result = 3*n+1	# create a variable called result
		return result	# return result
	else:
		result = n/2	# create a variable called result
		return result	# return result


print(colatz(2))