import csv

path = '../Resources/budget_data.csv'

months = 0
profit_loss = 0
previous_month_profit_loss = 0
changes_in_profit_loss = []
greatest_increase = ['', -float('inf')]
greatest_decrease = ['', float('inf')]

with open(path, newline = '') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')


    next(csvreader)

    for row in csvreader:
        months += 1

        profit_loss += int(row[1])

        change_in_profit_loss = int(row[1]) - previous_month_profit_loss

        changes_in_profit_loss.append(change_in_profit_loss)

        if change_in_profit_loss > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change_in_profit_loss
        elif change_in_profit_loss < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change_in_profit_loss

        previous_month_profit_loss = int(row[1])

average_change = sum(changes_in_profit_loss[1:]) / len(changes_in_profit_loss[1:])

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${profit_loss}")
print(f"Average Change: ${round(average_change, 2)}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

with open("results.txt", "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("----------------------------\n")
    text_file.write(f"Total Months: {months}\n")
    text_file.write(f"Total: ${profit_loss}\n")
    text_file.write(f"Average Change: ${round(average_change, 2)}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
