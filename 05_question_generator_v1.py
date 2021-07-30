import random

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

# Generate users questions below...
print("*Question one*")
Question = num_check("What is 4 + 2 = ", 0, 10 )

print("Correct!")

print("*Question two*")
Question = num_check("What is 6 + 2 = ", 0, 10 )

print("Correct")

print("*Question Three*")
Question = num_check("What is 3 + 2 = ", 0, 10 )

print("Correct")
