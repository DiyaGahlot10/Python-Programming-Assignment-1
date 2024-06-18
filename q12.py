#Write a python program that calculates the sum of the digits of a given number.

num=int(input("Enter the Number :"))

sum=0
original_num=num


while num>0 :
    sum=sum+num%10
    num=int(num/10)

print("The sum of digits of ",original_num,"is ",sum)



