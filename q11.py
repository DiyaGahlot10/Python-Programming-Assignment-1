#Write a python program that generates the first n numbers in the Fibonacci sequence.

n1=0

n2=1

n=int(input("Enter How many fibonacci number you want: "))
print(n1)
for i in range(0,n-1):
    print(n2)
    n1,n2=n2,n1+n2