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
print("**** This is a 10 Question addition quizz ****")
low_num = num_check("What is the lowest number for a question? ", -500, 500)
high_num = num_check("What is the highest number for a question? ", low_num, 1000)

# Rounds won will be calculated (total - correct - incorrect)
questions_correct = 0
questions_incorrect = 0

game_summary = []

rounds = 10

	# Start of Game Play Loop

	# Rounds Heading for continuous mode / specific # of rounds
print()
if rounds == "":
	heading = "continuous Mode: Round {}".format(questions_correct + 1)
else:   
 heading = "Question 1 of 10".format(questions_incorrect + 1)
 

print(heading)
for item in range(0, 10):

	num_1 = random.randint(1, 10)
	num_2 = random.randint(1, 10)

	print("*Question*")
	question = "{} + {}".format(num_1, num_2)
	answer = eval(question)

	user_ans = int(input("What is {} = ".format(question)))

	if user_ans == answer:
		print("Correct!, Well Done :)")
		questions_correct += 1

	else:
		print("incorrect, Nice Try :(")
		questions_incorrect += 1

print("Game Over!")
print("*** Here are your results ***")


feedback ="questions correct: {} questions incorrect: {}".format(questions_correct,questions_incorrect)
print(feedback)
print()


# add result to list....
game_summary.append(feedback)