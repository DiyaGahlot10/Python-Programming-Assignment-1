#Write a python program that checks if two strings are anagrams of each other.


def calculate_frequency(string):
    frequency={}
    
    for char in string:
        if(char in frequency):
            frequency[char]+=1

        else:
            frequency[char]=1

    return frequency 

string_input1=input("Enter first string : ")

string_input2=input("Enter second string : ")

frequency1=calculate_frequency(string_input1)

frequency2=calculate_frequency(string_input2)

if(frequency1==frequency2):
    print(string_input1,"and",string_input2,"are anagrams")

else:
    print("Given inputs are not anagrams")