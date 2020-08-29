a = 33 
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a equals b")


'''Ex1)
 Create a program to ask two numbers
number1-----9
number2-----12
compare the number and show the bigger number on your screen
"between 9 and 12, 12 is bigger"

'''

number1 = int(input("Number1?"))
number2 = int(input("Number2?"))

if number1 < number2:
    print("between " + str(number1) + " and " + str(number2) + ", " + str(number2) + " is bigger.")
elif number1 > number2:
    print("between " + str(number1) + " and " + str(number2) + ", " + str(number1) + " is bigger.")

'''Ex2)
Create a program to ask three subjets
math
science
english
name

average
<70-----"You failed"
>=80-----$500
>=90-----$1000
>=100-----$10000

Tell him 
"John, your average for math, science, english are 90, 80, 70 is 80. 
So, you passed the course and will get a scholarship of $500"

)
'''
name = input("What is your name?")
math = int(input("math?"))
science = int(input("english?"))
english = int(input("physics?"))
average = (math + science + english)/3
if avarage <70:
    print(" You failed")
elif average >70:
    print(name + ", your average for math, science, english are " + str(math) + ", " + str(science) + ", " + str(english)+ ", is " +str(average) + ". So, you passed the course and will get a scholarship of $500")
elif average >80:
    print(name + ", your average for math, science, english are " + str(math) + ", " + str(science) + ", " + str(english)+ ", is " +str(average) + ". So, you passed the course and will get a scholarship of $500")