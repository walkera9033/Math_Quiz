import random

# functions go here...
def yes_no(question):
	valid = False
	while not valid: 
		response = input(question).lower() 
 
		if response == "yes" or response == "y":
				response = "yes"
				return response
				
		elif response == "no" or response == "n":
				response = "no"
				return response
				
		else:
			print("please answer yes/no")


def instructions():
	print ("**** How to Play ****") 
	print()
	print("in this paticular addition game the aim is to answer as many addition questions as you can correctly.")
	print () 
	return "" 


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
	instructions()
 
elif played_before == "yes": 
	print("program continues")
def num_check(question, low, high):
	error = "Please enter a whole number between low and high\n"

	valid = False 
	while not valid:
		try:
			# Ask the question 
			response = int(input(question))
			# if the amount is too low / too high give 
			if low < response <= high:
				return response

			# output an error
			else:
				print(error)

		except ValueError:
				print(error)


# Main routine go here
how_many = num_check("How many addition questions would you like to answer? ", 0, 10 )
low_num = num_check("What is the lowest number for a question? ", -500, 500)
high_num = num_check("What is the highest number for a question? ", low_num, 1000)

