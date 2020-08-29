def max_of_two(a, b):
    if a > b:
        return a
    return b
def max_of_three(a, b, c):
    return max_of_two(a, max_of_two(b, c))
print(max_of_three(5, 8, -9))

#Define function
def addNumbers(numbers):
    #Initialization of variable is very important
    total = 0
    for number in numbers:
        total += number
    return total
print(addNumbers((3,6,8,9,0,7)))

#Muntiply numbers
def multplyNumbers(numbers):
    total = 1
    for number in numbers:
        total *= number
    return total
print(multplyNumbers((1,3,5,7,8)))

'''Create a function to reverse a string. You need a return and use while loop
you need to initialization string as well
for example '1234abcd' ---> 'dcba4321'
Hint is index '''
    