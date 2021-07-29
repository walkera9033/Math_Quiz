import random

number_1 = random.randint(1, 10)
number_2 = random.randint(1, 10)


answer = eval("{} + {}".format(number_1, number_2))

print("{} + {}".format(number_1, number_2))
print("answer", answer)
