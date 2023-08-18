import math
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
def sine(a):
    return math.sin(a)
def cosine(a):
    return math.cos(a)
def tangent(a):
    return math.tan(a)
def logarithm(a,b):
    return math.log(a,b)
def power(a,b):
    return math.pow(a,b)
def squareroot(a):
    return math.sqrt(a)
def exponential(a):
    return math.exp(a)
def degree(a):
    return math.degrees(a)
def radian(a):
    return math.radians(a)
def fact(a):
    return math.factorial(a)

print("Select the operation you want to perform:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.sin")
print("6.cos")
print("7.tan")
print("8.log")
print("9.power")
print("10.squareroot")
print("11.Exponent")
print("12.Degree")
print("13.Radian")
print("14.Factorial")

while True:
    choice=input("Enter your choice number:")
    if choice in ('1','2','3','4','8','9'):
        num1=float(input("Enter the first number:"))
        num2=float(input("Enter the second number"))
    elif choice in ('5','6','7','10','11','12','13','14'):
        num3=float(input("Enter the number:"))
    else:
        print("Invalid Choice")
    if choice=='1':
        print(num1,"+",num2,"=",add(num1,num2))
    elif choice=='2':
        print(num1,"-",num2,"=",subtract(num1,num2))
    elif choice=='3':
        print(num1,"*",num2,"=",multiply(num1,num2))
    elif choice=='4':
        print(num1,"/",num2,"=",divide(num1,num2))
    elif choice=='5':
        print("sin of ",num3,"is",sine(num3))
    elif choice=='6':
        print("cos of ",num3,"is",cosine(num3))
    elif choice=='7':
        print("tan of ",num3,"is",tangent(num3))
    elif choice=='8':
        print("log of ",num1,"with base ",num2,"is",logarithm(num1,num2))
    elif choice=='9':
        print(num1,"to power ",num2,"is",power(num1,num2))
    elif choice=='10':
        print("Squareroot of ",num3,"is",squareroot(num3))
    elif choice=='11':
        print("e to power ",num3,"is",exponential(num3))
    elif choice=='12':
        print("Degree of",num3,"is",degree(num3))
    elif choice=='13':
        print("Radian of ",num3,"is",radian(num3))
    elif choice=='14':
        print("Factorial of ",(num3),"is",fact(int(num3)))
    break
