import csv
import os

voter = 0
khan = 0
correy = 0
li = 0
OTooley = 0


# read csv file
with open('Resources/election_data.csv', newline='', encoding="utf-8") as FreeBritney:

    # Create variable to store contents of budget_data.csv
    Free = csv.reader(FreeBritney, delimiter = ',')
    
    # Start the second row by skipping the first row
    Britney = next(FreeBritney)
    
    # Iterate through the rows in the stored file contents
    for row in Free:
        # Total votes
        voter +=1
        
        # IF statement to count number of vote casted for each candidate
        if row[2] == "Khan":

            khan +=1

        elif row[2] == "Correy":

            correy +=1

        elif row[2] == "Li":

            li +=1

        elif row[2] == "O'Tooley":

            OTooley +=1
            
 # create a dictionary dedicate the list of candidates and number of votes for each candidate

candidates = ["Khan", "Correy", "Li","O'Tooley"]

votes = [khan, correy, li, OTooley]

# We zip them together in a list

# Return the winner using a max function of the dictionary to get the highest percentage of the vote

OopsIDidItAgain = dict(zip(candidates,votes))

Lucky = max(OopsIDidItAgain, key=OopsIDidItAgain.get)


# Print a the summary of the analysis

khan_percent = (khan/voter) *100

correy_percent = (correy/voter) * 100

li_percent = (li/voter) * 100

otooley_percent = (OTooley/voter) * 100

print('Election Results')

print("----------------------------")

print(f"The total number of votes cast is: {voter}")

print("----------------------------")

print(f"Khan: {khan_percent:.3f} % ({khan})")

print(f"Correy: {correy_percent:.3f} % ({correy})")

print(f"Li: {li_percent:.3f} % ({li})")

print(f"O'Tooley: {otooley_percent:.3f} % ({OTooley})")

print("----------------------------")

print(f"The Winner is: {Lucky}")
print(f"----------------------------")

# export a text file with the results.

from pathlib import Path

output = Path("Resources", "Eletion Results.txt")

with open(output,"w") as analysis:
    
    # Print results to txt file
    analysis.write("Election Results")
    analysis.write("\n")
    analysis.write("----------------------------")
    analysis.write("\n")
    analysis.write(f"The total number of votes cast is: {voter}")
    analysis.write("\n")
    analysis.write("----------------------------")
    analysis.write("\n")
    analysis.write(f"Khan: {khan_percent:.3f} % ({khan})")
    analysis.write("\n")
    analysis.write(f"Correy: {correy_percent:.3f} % ({correy})")
    analysis.write("\n")
    analysis.write(f"Li: {li_percent:.3f} % ({li})")
    analysis.write("\n")
    analysis.write(f"O'Tooley: {otooley_percent:.3f} % ({OTooley})")
    analysis.write("\n")
    analysis.write("----------------------------")
    analysis.write("\n")
    analysis.write(f"The Winner is: ({Lucky})")
    analysis.write("\n")
    analysis.write("----------------------------")
