from random import randint  # use randint(a, b) to generate a random number between a and b

number = 0 # store random number in here, each time through
i = 0  # i should be incremented by one each iteration
#your answer  goes here
while number != 5:
    print(number)
    i += 1
    number = randint(1, 11)