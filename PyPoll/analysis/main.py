import os
import csv

csvpath = os.path.join('../Resources/election_data.csv')

total_votes = 0
candidates = {}
winner = ""
winner_votes = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] not in candidates:
            candidates[row[2]] = 1
        else:
            candidates[row[2]] += 1

output_file = open("results.txt", "w")

output_file.write("Results\n")
output_file.write("-------------------------\n")
print("Election Results")
print("-------------------------")

output_file.write(f"Total Votes: {total_votes}\n")
print(f"Total Votes: {total_votes}")
output_file.write("-------------------------\n")
print("-------------------------")


for candidate, votes in candidates.items():
    percentage = round((votes / total_votes) * 100, 3)
    output_file.write(f"{candidate}: {percentage}% ({votes})\n")
    print(f"{candidate}: {percentage}% ({votes})")

    if votes > winner_votes:
        winner = candidate
        winner_votes = votes

output_file.write("-------------------------\n")
print("-------------------------")
output_file.write(f"Winner: {winner}\n")
print(f"Winner: {winner}")
output_file.write("-------------------------\n")
print("-------------------------")


output_file.close()
