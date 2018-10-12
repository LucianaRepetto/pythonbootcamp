#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)

#yo respondi
def generate_evens():
    evens=[]
    for num in range(1,50):
        if num%2 == 0:
            evens.append(num)
    return evens

# si hubiera usado list comprehension
def generate_evens7():
    return [num for num in range(1,50) if num % 2 == 0]