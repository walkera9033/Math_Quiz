questions_correct = 0
questions_incorrect = 0
for item in "results":
	questions_correct += 1
if item == "Correct":
	result = "its a correct"
	questions_incorrect += 1
elif item == "incorrect":
	result = "its incorrect"

