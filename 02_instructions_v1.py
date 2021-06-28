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
	print ("In this paticular addition game the aim is to answer as many addition questions as you can correctly.")
	print () 
	return "" 


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
	instructions()
 
elif played_before == "yes": 
	print("program continues")

