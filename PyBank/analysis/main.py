import csv

# define the input file path
file_path = '/Reources/budget_data.csv'

# initialize variables
total_months = 0
total_profit = 0
profit_changes = []
previous_profit = 0
greatest_increase = ['', 0]
greatest_decrease = ['', 9999999999999999999]

# read the CSV file
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    # skip header row
    header = next(csvreader)
    # loop through each row in the CSV file
    for row in csvreader:
        # count the total number of months
        total_months += 1
        # calculate the total amount of profit/losses
        total_profit += int(row[1])
        # calculate the change in profit/losses from the previous month
        profit_change = int(row[1]) - previous_profit
        # store the profit change in a list
        profit_changes.append(profit_change)
        # update the previous profit variable
        previous_profit = int(row[1])
        # find the greatest increase in profits
        if profit_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change
        # find the greatest decrease in profits
        if profit_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change

# calculate the average change in profit/losses
average_change = sum(profit_changes[1:]) / len(profit_changes[1:])

# print the results
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')