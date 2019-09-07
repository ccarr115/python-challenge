# import os and csv modules
import os
import csv

# connect to data
Budget_data = os.path.join('..', 'PyBank', 'Budget_data.csv')

with open(Budget_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    rows_count = 0
    net_profit = 0
    month_list = []
    profit_list = []
    monthly_revenue_changes = []

#  calculate total number of months included in the dataset
    # loop through each row
    for row in csvreader:
        # add 1 for each row in loop (total # of row = total months)
        rows_count = rows_count + 1

# calculate net total amount of "Profit/Losses" over the entire period
        # sum column 2
        net_profit = net_profit + int(row[1])

# calculate average of the changes in "Profit/Losses" over the entire period

        # append all of the values to make an indexed list
        profit_list.append(row[1])
        month_list.append(row[0])

    for i in range(1,len(profit_list)):
        # calculate difference in profit values between rows, and populate monthly rev change list with those values
        monthly_revenue_changes.append(int(profit_list[i]) - int(profit_list[i-1]))   
        # calculate mean by summing the list and then dividing by it's length
        avg_rev_change = sum(monthly_revenue_changes)/len(monthly_revenue_changes)

# identify the greatest increase in profits (date and amount) over the entire period
#    
        max_rev_change = max(monthly_revenue_changes)
        max_index = monthly_revenue_changes.index(max_rev_change)
        max_month = month_list[max_index + 1]

# identify the greatest decrease in losses (date and amount) over the entire period       
       
        # now do all of the same steps for the min values
        min_rev_change = min(monthly_revenue_changes)
        min_index = monthly_revenue_changes.index(min_rev_change)
        min_month = month_list[min_index + 1]

# print analysis summary to terminal  
  
    print("Financial Analysis")
    print("-------------------------------------------------------------------")
    print(f"Total Months:{rows_count}")
    print(f"Total: ${net_profit}")
    # the :.2F code tells python to limit the number (a float, see above) to just 2 decimal places
    print(f"Average Change: ${avg_rev_change:.2F}")
    print(f"Greatest Increase in Profits: {max_month} (${max_rev_change})")
    print(f"Greatest Decrease in Profits: {min_month} (${min_rev_change})")

# ---------------------------------------------------------------------------
# TASK #7 export results to a text file
# ---------------------------------------------------------------------------

file = open("PyBankResults.txt", "w+")

file.write("Financial Analysis\n")
file.write("-------------------------------------------------------------------\n")
file.write(f'Total Months: {rows_count}\n')
file.write(f'Total: ${net_profit}\n')
file.write(f'Average Change: ${avg_rev_change:.2F}\n')
file.write(f'Greatest Increase in Profits: {max_month} (${max_rev_change})\n')
file.write(f'Greatest Decrease in Profits: {min_month} (${min_rev_change})')
