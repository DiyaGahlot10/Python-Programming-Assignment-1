#Write a program in python that counts the frequency of each character in a string.

string_input=input("Enter a string :")
string_input=string_input.lower()
frequency={}

for char in string_input:
    if(char in frequency):
        frequency[char]+=1

    else:
        frequency[char]=1

print(frequency)


