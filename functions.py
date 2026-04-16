import utils  as utilityFunctionality
import math 
from math  import sqrt,tan, cos,sin

def getSumOfNumbers(firstNumber,secondNumber):
      sumOfNumbers = firstNumber + secondNumber
      return sumOfNumbers


firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))

sumOfTwoNumbers=getSumOfNumbers(firstNumber,secondNumber)
print("Sum of two numbers is: ",sumOfTwoNumbers)


squareOfNumber= firstNumber ** 2
print("Square of first number is: ",squareOfNumber)

#lambda function example
squareOfNumber = lambda x: x * x
number = int(input("Enter a number to find its square: "))
print("Square of the number is: ", squareOfNumber(number))

#lambda function to sort the value
employees = [
    ("John", 50000),
    ("Sara", 60000),
    ("Mike", 45000)
]

sorted_list = sorted(employees, key=lambda x: x[1])
print(sorted_list)


utilityFunctionality.calculateSalary(15, 40)

math.sqrt(16)
