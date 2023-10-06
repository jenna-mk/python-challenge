import csv
import os

# ------------------------------
# ANALYSIS
# ------------------------------

# Set file paths for reading/writing
election_data = os.path.join('Resources', 'election_data.csv')

# Set variables and create empty lists to iterate through correct rows 
votes = []
candidates = [] 

# Create an empty dictionary to track the candidates and their total number of votes
candidate_votes = {}

# Open and read the election data file
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip header row
    csv_header = next(csvreader)

    # Begin for loop for analysis 
    for row in csvreader:
 
        # Transfer the ballot ID to the votes list, and take the length to get total number of votes 
        votes.append(row[0])
        total_votes = len(votes)

        # Iterate through the candidate column to get unique names 
        # Code inspiration taken from Larson, 2022
        candidate_name = row[2]
        # If the candidate is not already listed, add them to the candidates list
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            # Add them to the dictionary (with initial votes of 0) to track their votes as for loop runs
            candidate_votes[candidate_name] = 0
        # Each time the candidate is found, add one vote to their dictionary value
        candidate_votes[candidate_name] += 1

        # Find the vote count for each unique candidate
        for candidate in candidate_votes:
            vote_count = candidate_votes[candidate]

# Find the maximum value from the dictionary of candidates and their vote count       
winner = max(candidate_votes, key=candidate_votes.get)

# Split candidate names dictionary into lists and use the values to calculate the percentage of votes for each individual candidate
# Storing the candidate names, candidate votes, and percentage for each in lists allows us to zip together and print in f string

# Convert the vote values into a list
voting = list(candidate_votes.values())
# Calculate the percentage from the voting list and store in a new percentage votes list
percentage_votes = [(x / total_votes) * 100 for x in voting]
# Store the candidate names in a list 
name = list(candidate_votes.keys())

# ------------------------------
# SUMMARY TABLE
# ------------------------------
   
# Print the election results
print("Election Results")
print("------------------------------")
print(f'Total Votes: {total_votes}')
print("------------------------------")
# Use a for loop to iterate through key, value pairs in the candidate_votes dictionary and print the results
# Code inspiration taken from Stewart, 2019
for (candidate, final_vote_count, pct_vote) in zip(name, voting, percentage_votes):
    print(f'{candidate}: {pct_vote: .3f}% ({final_vote_count})')
print("------------------------------")
print(f'Winner: {winner}')
print("------------------------------")

# ------------------------------
# OUTPUT FILE
# ------------------------------

# Create output file path
election_output = os.path.join('analysis', 'election_results_summary.txt')

# Open the file for writing
with open(election_output, 'w') as f:
    f.write("Election Results")
    f.write("\n")
    f.write("------------------------------")
    f.write("\n")
    f.write(f'Total Votes: {total_votes}')
    f.write("\n")
    f.write("------------------------------")
    f.write("\n")
    for (candidate, final_vote_count, pct_vote) in zip(name, voting, percentage_votes):
        f.write(f'{candidate}: {pct_vote: .3f}% ({final_vote_count}) \n')
    f.write("\n")
    f.write("------------------------------")
    f.write("\n")
    f.write(f'Winner: {winner}')
    f.write("\n")
    f.write("------------------------------")



# REFERENCES
# Larson, Mychele (2022) Python_Analysis. GitHub repository, https://github.com/mychele-larson/Python_Analysis/tree/main
# Stewart, L (2019) python-challenge. GitHub repository, https://gitlab.com/laurelstewart/python-challenge