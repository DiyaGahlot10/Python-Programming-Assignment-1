#Write a python program that takes a list of numbers and returns their sum.

n=int(input("Enter number of elements you want in list :"))
lst=[]
sum=0
for i in range(0,n):
    print("Enter element",i+1,":")
    x=int(input())
    lst.append(x)
    sum+=x
print("The list is",lst)
print("The sum of elements of list",sum)
