def useless(one,two,three):
    return str("That was a waste of time")

print(useless(1,2,3))
print(useless("Hello","Goodbye",3))

'''
square_me = 3
number = square_me ** 2
print(number)
'''
def square_me(number):
    return number **2


print(square_me(3))
print(square_me(9.5))

'''
list = (name,age,studentnumber,enrolled):
    name = str()
    age = int()
    studentnumber = int()
    enrolled = bol()
    print("str(studentnumber)"+ "str(name)"+ "str(age)"+"str(enrolled)")
'''

def student_data(name, age, number, enrolled):
    return "<"+number + "," + name + "," + str(age) + "," + str(enrolled)+">"

    
print(student_data("Brian",35,"1234567",False)) 