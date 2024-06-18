#Write a program that reads data from a CSV file and prints it to the console.

import csv

filename = "data.csv"

file = open(filename, "r")

csv_reader = csv.reader(file)

for row in csv_reader:
    print(row)


file.close()
