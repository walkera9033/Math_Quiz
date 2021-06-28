# Functions go here
def num_check(question, low, high):
	error = "Please enter an whole number be between 1 and 10"

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

