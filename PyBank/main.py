import csv
import os

# ------------------------------
# ANALYSIS
# ------------------------------

# Set file path 
budget_data = os.path.join('Resources','budget_data.csv')

# Set variables and create empty lists to iterate through rows
months = []
profit_loss = []
profit_change = []

# Open and read the budget file 
with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip header row 
    csv_header = next(csvreader)

    # Begin for loop for analysis 
    for row in csvreader:
        # Iterate through each row and transfer to list 
        months.append(row[0])
        profit_loss.append(int(row[1]))

        # Find the total number of months 
        total_months = len(months)

        # Find the net total of profits and losses        
        net_total = sum(profit_loss)
    
    # Iterate through the profits and losses to find the change month to month 
    # We subtract one from the range to account for the fact that we are looking at the NEXT month minus the current 
    # Code inspiration taken from cantugabriela, 2018 
    for month in range(len(profit_loss)-1):
        # Find the change in profit from one month to the next and add to the change in profit list 
        profit_change.append(profit_loss[month+1] - profit_loss[month])
    
    # Find the average change in profit over the entire period by summing the profit changes and dividing by the total number of months 
    profit_average = (sum(profit_change)) / (total_months)

# Find the greatest increase in profits by finding the maximum value in the profit change list 
max_increase = max(profit_change)

# Find the greatest decrease in profits by finding the minimum value in the profit change list 
max_decrease = min(profit_change)

# Find the correct indices of the profit change list that correspond to the maximum increase and decrease of profit
# Code inspiration taken from cantugabriela, 2018
max_increase_month = profit_change.index(max(profit_change)) + 1
max_decrease_month = profit_change.index(min(profit_change)) + 1        

# ------------------------------
# SUMMARY TABLE 
# ------------------------------

# Print the results for each calculation 
print("Financial Analysis")
print("------------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: {round(profit_average, 2)}')
# Find the index for max/min decrease to the list of months and add one to get the correct month in which the change occurred
print(f'Greatest Increase in Profits: {months[max_increase_month]} (${max_increase})')
print(f'Greatest Decrease in Profits: {months[max_decrease_month]} (${max_decrease})')

# ------------------------------
# OUTPUT FILE
# ------------------------------

# Create output file path 
budget_output = os.path.join('analysis', 'budget_results_summary.txt')

# Open file for writing 
with open(budget_output, 'w') as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("------------------------------")
    f.write("\n")
    f.write(f'Total Months: {total_months}')
    f.write("\n")
    f.write(f'Total: ${net_total}')
    f.write("\n")
    f.write(f'Average Change: {round(profit_average, 2)}')
    f.write("\n")
    f.write(f'Greatest Increase in Profits: {months[max_increase_month]} (${max_increase})')
    f.write("\n")
    f.write(f'Greatest Decrease in Profits: {months[max_decrease_month]} (${max_decrease})')

# REFERENCES 
# cantugabriela (2018) Python-Challenge. GitHub repository, https://github.com/cantugabriela/Python-Challenge