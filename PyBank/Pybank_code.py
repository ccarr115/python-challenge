import os
import csv
f = open("Budget_data.csv")
pybank_csv_path = os.path.join("Budget_data.csv")
file_output = "pybank_results.txt"
total_months = 0
total_revenue = 0
months_of_change =  []
previous_revenue = 0
revenue_change_list = []
greatest_increase = ["",0]
greatest_decrease = ["",99999999999]
with open(pybank_csv_path,newline="") as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        total_months = total_months + 1
        total_revenue = total_revenue + int(row["Revenue"])
        previous_revenue = int(row["Revenue"])
        revenue_change = int(row["Revenue"])- previous_revenue
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]
if revenue_change <greatest_decrease[1]:
    greatest_decrease[1]= revenue_change
    greatest_decrease[0] = row['Date']

#print(rev_change_list)
rev_avg = sum(revenue_change_list)/len(revenue_change_list)


print('Average Change in Revenue: $ ' + str(rev_avg))
print("Total Months: " + str(total_months))
print("Total Revenue: $ " + str(total_revenue))
print(greatest_increase)
print(greatest_decrease)

if revenue_change<greatest_decrease[1]:
    greatest_decrease[1]= revenue_change
    greatest_decrease[0] = row['Date']

#print(rev_change_list)
rev_avg = sum(revenue_change_list)/len(revenue_change_list)


print('Average Change in Revenue: $ ' + str(rev_avg))
print("Total Months: " + str(total_months))
print("Total Revenue: $ " + str(total_revenue))
print(greatest_increase)
print(greatest_decrease)

with open(file_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total Revenue: $%d\n" % total_revenue)
    file.write("Average Revenue Change $%d\n" % rev_avg)
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))
