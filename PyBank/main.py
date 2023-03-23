import csv
import os

# Set path
budget_data = os.path.join("Resources","budget_data.csv")

# def vars
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_changes = []
months = []

# Open the CSV file and loop through the rows
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip head
    header = next(csvreader)
    # Loop through 
    for row in csvreader:
        # num of months counter
        total_months += 1
        # Net p/l count
        total_profit_loss += int(row[1])
        # active p/l counter
        profit_loss_change = int(row[1]) - previous_profit_loss
        previous_profit_loss = int(row[1])
        profit_loss_changes.append(profit_loss_change)
        months.append(row[0])

# Get avg
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

# Greatest increase profits
greatest_increase = max(profit_loss_changes)
greatest_increase_index = profit_loss_changes.index(greatest_increase)
greatest_increase_month = months[greatest_increase_index + 1]

# Greatest decrease profits
greatest_decrease = min(profit_loss_changes)
greatest_decrease_index = profit_loss_changes.index(greatest_decrease)
greatest_decrease_month = months[greatest_decrease_index + 1]

# Print financial analysis 
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")

# Export file
output_file = "financial_analysis.txt"
with open(output_file, "w") as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("------------------------\n")
    text_file.write(f"Total Months: {total_months}\n")
    text_file.write(f"Total: ${total_profit_loss}\n")
    text_file.write(f"Average Change: ${average_change:.2f}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")
