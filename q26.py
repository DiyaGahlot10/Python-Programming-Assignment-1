#Write a program in python that checks if a string starts with a given prefix or ends with a given suffix.
string_input=input("Enter the string : ")

prefix=input("Enter the prefix you want to check  : ")
suffix=input("Enter the suffix you want to check  : ")

if (string_input.startswith(prefix)):
    print("Prefix is present in the string")
if (string_input.endswith(suffix)):
    print("Suffix is presnt in the string")
else:
    print("NO perfix or suffix found in string")
