#Write a python program that counts the occurrences of a specific element in a list.

n=int(input("Enter number of elements you want in list :"))
lst=[]

for i in range(0,n):

    x=int(input())
    lst.append(x)

search_element=int(input("Enter you want to occurrences :"))

count=0

for i in lst:
    if(i==search_element):
        count=count+1

    else:
        pass
print("The occurrence of",search_element,"in the list",lst,"are",count)
