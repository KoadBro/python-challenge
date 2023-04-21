import os
import csv

# Set path for file
csvpath = os.path.join('../Resources/election_data.csv')

# Initialize variables
total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

# Read the CSV file
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Loop through each row in the CSV file
    for row in csvreader:
        # Increment the vote counter
        total_votes += 1

        # If this candidate hasn't been seen before, add them to the dictionary
        if row[2] not in candidates:
            candidates[row[2]] = 1
        # Otherwise, increment the vote count for this candidate
        else:
            candidates[row[2]] += 1

# Open the output file
output_file = open("results.txt", "w")

# Print the results to the terminal and write to the output file
output_file.write("Results\n")
output_file.write("-------------------------\n")
print("Election Results")
print("-------------------------")
output_file.write(f"Total Votes: {total_votes}\n")
print(f"Total Votes: {total_votes}")
output_file.write("-------------------------\n")
print("-------------------------")

# Loop through the candidates and calculate their percentage of votes
for candidate, votes in candidates.items():
    percentage = round((votes / total_votes) * 100, 3)
    output_file.write(f"{candidate}: {percentage}% ({votes})\n")
    print(f"{candidate}: {percentage}% ({votes})")

    # If this candidate has more votes than the current winner, update the winner
    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

output_file.write("-------------------------\n")
print("-------------------------")
output_file.write(f"Winner: {winner}\n")
print(f"Winner: {winner}")
output_file.write("-------------------------\n")
print("-------------------------")

# Close the output file
output_file.close()
