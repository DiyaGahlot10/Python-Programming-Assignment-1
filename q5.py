#Write a program that takes a string input from the user and writes it to a text file.



user_input = input("Enter a string to be written to the file: ")

file = open("C:/Users/Paras Gahlot/OneDrive/Desktop/Assignment-Ai-Ml internship/Python Programming Assignment-1/output.txt", "w")


file.write(user_input)


file.close()

print("The string has been written to file")
