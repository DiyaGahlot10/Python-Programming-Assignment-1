#Write a program that acts as a simple calculator. It should take two numbers and an operator (+, -, *, /) as input and print the result.

num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))

operator=input("Enter the opreation you want to perform :")

if(operator=="+"):
    print("sum of the numbers are:",num1+num2)

elif(operator=="-"):
    
    print("subtraction of the numbers are:",num1-num2)
elif(operator=="*"):
    
    print("mutiplication of the numbers are:",num1*num2)

elif(operator=="/"):
    
    print("division of the numbers are:",num1/num2)

else:
    print("Invalid operator!!")
    


