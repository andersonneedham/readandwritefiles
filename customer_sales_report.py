import csv


sales_file = open("sales.csv", "r")
sales_reader = csv.reader(sales_file)


# CREATING NEW FILE TO HOUSE CUSTOMER ID AND CALCULATED TOTAL
sales_report = open("salesreport.csv", "w")
salesnew_reader = csv.writer(sales_report, delimiter="\t")


# THE NEW COLUMN HEADERS FOR SALESREPORT.CSV FILE
salesnew_reader.writerow(["Customer ID:" "\t\t" "Calculated Total:"])


for line in sales_reader:
    if line[3] == "SubTotal":
        continue
    total = round(float(line[3]) + float(line[4]), 2)
    salesnew_reader.writerow(
        ["Customer ID: " + line[0] + "\t" + "Calculated Total: " + str(total)]
    )


sales_file.close
sales_report.close
