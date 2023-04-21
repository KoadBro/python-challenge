import csv

path = '../Resources/budget_data.csv'

total_months = 0
total_profit = 0
profit_changes = []
previous_profit = 0
greatest_increase = ['', -float('inf')]
greatest_decrease = ['', float('inf')]

with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
    for row in csvreader:

        total_months += 1
        total_profit += int(row[1])
        profit_change = int(row[1]) - previous_profit
        profit_changes.append(profit_change)
        previous_profit = int(row[1])

        if profit_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = profit_change

        if profit_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = profit_change

average_change = sum(profit_changes[1:]) / len(profit_changes[1:])

print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${total_profit}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})')
print(f'Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})')