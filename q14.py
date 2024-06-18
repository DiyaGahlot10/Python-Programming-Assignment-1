#Write a program that reads multiple lines of input from the user until they enter an empty line, then prints all the lines.

lines=[]

print("Enter line or press enter if you want to stop :")

while True:
    line=input()
    if(line==""):
        break

    else:
        lines.append(line)

for line in lines:
    print(line)
