# Modules
import os
import csv

CSV_PATH = os.path.join('Resources', 'election_data.csv')

# Set variable
total_num_votes = 0
candidate_votes = {}
votes = 0 
winning_candidate = ""
winning_count = 0

os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)    #pull out header row

    for row in csvreader:
        #Count total number of votes cast
        total_num_votes += 1
        #Make dictionary of vote counts
        candidate_name = row[2]
        #loop through votes and update vote count for each candidate
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] +=1 
        else: 
            candidate_votes[candidate_name] = 1
    #print header
    print("Elections votes: ")
    #print total number of votes cast
    print("Total votes:", total_num_votes)
    #print complete list of candidates who received votes
    print(candidate_votes)

# Open a text file for writing the results
with open("election_results.txt", "w") as file:
    file.write(f"Election Results\n\n")
    file.write(f"---------------------------\n\n")
    # Write the total number of votes cast to the file
    file.write(f"Total Votes: {total_num_votes}\n\n")
    file.write(f"---------------------------\n\n")

    #calculate percentage of votes for each candidate
    for candidate_name, votes in candidate_votes.items():
        percentage = (votes/total_num_votes)*100
        #print total number of votes per candidate and percentage
        print(f"{candidate_name}: {percentage:.2f}% ({votes})")
        # Write the list of candidates, percentage and number of votes to the file
        file.write(f"{candidate_name}: {percentage:.2f}% ({votes})\n\n")
        file.write(f"---------------------------\n\n")

    #Calculate winner of the election based on popular vote
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate_name
    print("Winner:", winning_candidate)
    #Write winner
    file.write(f"Winner: {winning_candidate}\n\n")
    file.write(f"---------------------------\n\n")
 
    # Print a message indicating that the results have been saved to the file
print("Election results have been saved to 'election_results.txt'.")