import csv
import os

months = []
profitnloss = []
average = []

# read csv file
with open('Resources/budget_data.csv', newline='', encoding="utf-8") as csvfile:

    # Create variable to store contents of budget_data.csv
    cardiB = csv.reader(csvfile, delimiter = ',')
    
    # Start the second row by skipping the first row
    WAP = next(csvfile)

    # Iterate through the rows in the stored file contents
    for row in cardiB:
        # executing the method append on the list the size of the list increases by one
        months.append(row[0])
        profitnloss.append(int(row[1]))

    # Iterate through the profits in order to get the monthly change in profits
    for i in range(len(profitnloss)-1):
        
        # Take the difference between two months and append to monthly profit change
        average.append(profitnloss[i+1]-profitnloss[i])

# The greatest increase in profits (date and amount) over the entire period
max_increase_value = max(average)

# The greatest decrease in losses (date and amount) over the entire period
max_decrease_value = min(average)

max_increase_month = average.index(max(average)) + 1
max_decrease_month = average.index(min(average)) + 1

print('Financial Analysis')

print('----------------------------')

print(f"The total number of months is: {len(months)}")

print(f"The Total net profit/Loss is: {sum(profitnloss)}")

print(f"Average Change: {round(sum(average)/len(average), 2)}")

print(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")

print(f"Greatest Decrease in losses: {months[max_decrease_month]} (${(str(max_decrease_value))})")


# export a text file with the results.

from pathlib import Path

output = Path("Resources", "Financial_Analysis_Summary.txt")

with open(output,"w") as analysis:
    
    # Print results to txt file
    analysis.write("Financial Analysis")
    analysis.write("\n")
    analysis.write("----------------------------")
    analysis.write("\n")
    analysis.write(f"Total Months: {len(months)}")
    analysis.write("\n")
    analysis.write(f"Total: ${sum(profitnloss)}")
    analysis.write("\n")
    analysis.write(f"Average Change: {round(sum(profitnloss)/len(profitnloss),2)}")
    analysis.write("\n")
    analysis.write(f"Greatest Increase in Profits: {months[max_increase_month]} (${(str(max_increase_value))})")
    analysis.write("\n")
    analysis.write(f"Greatest Decrease in losses: {months[max_decrease_month]} (${(str(max_decrease_value))})")
