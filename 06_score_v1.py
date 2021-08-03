
# Questions won will be calculated (total - correct - incorrect)
questions_correct = 0
questions_incorrect = 0

if user_ans == correct_answer:

	result = "right"
	question_correct += 1

 else:
	statement_generator("incorrect, Nice Try :(")
	result = "wrong"
	question_wrong -= 1