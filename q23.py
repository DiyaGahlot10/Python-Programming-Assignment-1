#Write a program that converts temperature from Celsius to Fahrenheit and vice versa based on user input.
temp=int(input("Enter temp in celsisus : "))
choice=input("write the unit in which you want the temp : ")

if choice.lower()=="celsius" :
    temp=(temp-32) * (5/9)

elif choice.lower()=="fahrenheit":
    temp=(9/5)*temp + 32

else:
    print("Invalid choice!!")

print(temp)



