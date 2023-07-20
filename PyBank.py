# Modules
import os
import csv

CSV_PATH = os.path.join('Resources', 'budget_data.csv')

#Set variable 
counter = 0
total_sum=0
greatestincrease = 0 
greatestdecrease = 0 
prevprofit = 0
changes = []

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #pull out first row
    next(csvreader)
    firstrow = next(csvreader)
    prevprofit = int(firstrow[1])
    counter += 1
    total_sum = int(firstrow[1])
    for row in csvreader:
        counter += 1
        total_sum = total_sum + int(row[1])
        if prevprofit != 0:
            changes.append(int(row[1])-prevprofit)
        if greatestincrease < int(row[1])-prevprofit:
            greatestincrease = int(row[1])-prevprofit 
        if greatestdecrease > int(row[1])-prevprofit:
            greatestdecrease = int(row[1])-prevprofit   
        prevprofit = int(row[1])             
changetotal = 0
for change in changes:
    changetotal += change
ave_of_changes = changetotal / len(changes)
     
print(counter) 
print(total_sum)
print(ave_of_changes)
print(greatestincrease)
print(greatestdecrease)

# Open a text file for writing the results
with open("financial_analysis.txt", "w") as file:
    # Write financial analysis to the file
    file.write(f"Financial Analysis\n\n")
    file.write(f"---------------------------\n\n")
    file.write(f"Total Months: {counter}\n\n")
    file.write(f"Total: {total_sum}\n\n")
    file.write(f"Average Change: {ave_of_changes:.2f}\n\n")
    file.write(f"Greatest Increase: {greatestincrease}\n\n")
    file.write(f"Greatest Decrease: {greatestdecrease}\n\n")
# Print a message indicating that the results have been saved to the file
print("Financial Analysis have been saved to 'financial_analysis.txt'.")