#Write a program that copies the contents of one text file to another.

source_file = open("C:/Users/Paras Gahlot/OneDrive/Desktop/Assignment-Ai-Ml internship/Python Programming Assignment-1/output.txt", "r")

content = source_file.read()

source_file.close()


destination_file = open("C:/Users/Paras Gahlot/OneDrive/Desktop/Assignment-Ai-Ml internship/Python Programming Assignment-1/newoutput.txt", "w")


destination_file.write(content)

destination_file.close()

print("The content has been copied from outputfile to newoutputfile")
