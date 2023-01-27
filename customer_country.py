import csv

# OPENING CUSTOMER CSV FILE
customers = open("customers.csv", "r")
# CREATING NEW FILE?
customer_country = open("customer_country.csv", "w")

# NEW FILE COLUMN HEADERS
customer_country.write("FirstName\t| LastName\t| Country \n")

# READING CUSTOMER.CSV
csv_customers = csv.reader(customers)

# SKIPPING COLUMN HEADERS
next(csv_customers)

for row in csv_customers:
    customer_country.write(row[1] + "\t\t" + row[2] + "\t\t" + row[4] + "\n")

customers.close()
customer_country.close()
