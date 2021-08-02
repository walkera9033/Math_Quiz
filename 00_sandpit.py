import random

num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)

question = "{} + {}".format(num_1, num_2)
answer = eval(question)

user_ans = int(input("What is {} = ".format(question)))

if user_ans == answer:
	print("correct")
else:
	print("incorrect")