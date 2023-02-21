import csv

infile = open("customers.csv", "r")
csvfile = csv.reader(infile)

searchname = input(f"Please Enter the name to search for: ")
next(csvfile)  # skip the first line which is the header

foundFlag = False

for record in csvfile:
    if record[1].lower() == searchname.lower():
        print("Match Found")
        print()
        print(f"First Name: {record[1]}")
        print(f"Last Name: {record[2]}")
        print(f"City: {record[3]}")
        print(f"Country: {record[4]}")
        print(f"Phone: {record[5]}")
        foundFlag = True
if not foundFlag:
    print("Match not found")
