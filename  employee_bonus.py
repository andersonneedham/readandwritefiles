import csv

# READING EMPLOYEE PAY CSV
employee_info = open("EmployeePay.csv", "r")
reader = csv.reader(employee_info)

# loop through lines in file AND SKIP FIRST ROW?
next(reader)
for row in reader:
    print(
        "Employee ID: "
        + row[0]
        + ", Name: "
        + row[1]
        + " "
        + row[2]
        + ", Salary: "
        + row[3]
        + ", Bonus: "
        + row[4]
    )

employee_info.close()
