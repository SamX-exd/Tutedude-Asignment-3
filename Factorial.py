"""
Calculate Factorial Using a Function
"""


def factorial(a):

    if a == 1 :# base case

        return 1

    return a * factorial(a - 1)# recursive call

num = int(input("Enter the number:"))
result =  factorial(num)

print(result)

