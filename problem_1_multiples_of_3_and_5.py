# Multiples of 3 and 5
# Problem 1
	# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
	# Find the sum of all the multiples of 3 or 5 below 1000.

#!/usr/bin/env/python

# check if the given number is a multiple of 3 or 5
def check(ntrl_nos):
	flag = False
	if ((ntrl_nos % 3 == 0) or (ntrl_nos % 5 == 0)):
		flag = True
	return flag


# main function to retrieve numbers from 1-1000 and check if these are multiples of 3 or 5
def main():
	sum_of_ntrl_nos = 0
	for ntrl_nos in range(1, 1000):
		if (check(ntrl_nos)):
			sum_of_ntrl_nos = sum_of_ntrl_nos + ntrl_nos

	print(sum_of_ntrl_nos)


# calling the main function
main()