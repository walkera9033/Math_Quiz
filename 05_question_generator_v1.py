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
import random

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

print("*Question one*")
question = "{} + {}".format(num_1, num_2)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")


num_3 = random.randint(1, 10)
num_4 = random.randint(1, 10)

print("*Question two*")
question = "{} + {}".format(num_3, num_4)
answer = eval(question)

user_ans = int(input("what is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")


num_5 = random.randint(1, 10)
num_6 = random.randint(1, 10)

print("*Question three*")
question = "{} + {}".format(num_5, num_6)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")

num_7 = random.randint(1, 10)
num_8 = random.randint(1, 10)

print("*Question four*")
question = "{} + {}".format(num_7, num_8)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")

	
num_9 = random.randint(1, 10)
num_10 = random.randint(1, 10)

print("*Question five*")
question = "{} + {}".format(num_9, num_10)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
 print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")


num_11= random.randint(1, 10)
num_12 = random.randint(1, 10)

print("*Question six*")
question = "{} + {}".format(num_11, num_12)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")


num_13= random.randint(1, 10)
num_14 = random.randint(1, 10)

print("*Question seven*")
question = "{} + {}".format(num_13, num_14)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")


num_15= random.randint(1, 10)
num_16 = random.randint(1, 10)

print("*Question eight*")
question = "{} + {}".format(num_15, num_16)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")

	
num_17= random.randint(1, 10)
num_18 = random.randint(1, 10)

print("*Question nine*")
question = "{} + {}".format(num_17, num_18)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")
	
num_19= random.randint(1, 10)
num_20 = random.randint(1, 10)
	
print("*Question ten*")
question = "{} + {}".format(num_19, num_20)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("Correct!, Well Done :)")
else:
	print("incorrect, Nice Try :(")

print("Game Over!")






