#Write a python program that returns the minimum and maximum values in a list of numbers.

lst=[]
n=int(input("Enter number of elements in list :"))
for i in range(0,n):
    x=int(input())
    lst.append(x)

print("The list is ",lst)
print("the Maxmimum element in list is ",max(lst))
print("the Minimum element in list is ",min(lst))