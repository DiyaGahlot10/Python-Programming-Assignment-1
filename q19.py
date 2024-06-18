#Write a python program that removes all punctuation from a given string.

import string as st
string_input=input("Enter the string : ")

for ch in string_input:
    if ch in st.punctuation:
        string_input=string_input.replace(ch,"")
    else:
        pass

print(string_input)
