# number checking function
def num_check(question, low, high):
    error = "Please enter a whole number between low and high\n"
    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))
            # if the amount is too low / too high give
            if low < response <= high:
                return response
            # output an error
            else:
                print(error)
        except ValueError:
            print(error)

# main routine
low_num = num_check("What is the lowest number for a question? ", -500, 500)
high_num = num_check("What is the highest number for a question? ", low_num, 1000)
