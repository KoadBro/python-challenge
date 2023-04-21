import csv

total_votes = 0
candidates = {}
winner = ['', 0]

with open('../Resources/election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    next(csvreader)

    for row in csvreader:
        total_votes += 1

        if row[2] in candidates:
            candidates[row[2]] += 1
        else:
            candidates[row[2]] = 1

print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = round((votes / total_votes) * 100, 3)
    print(f"{candidate}: {percentage}% ({votes})")
    if votes > winner[1]:
        winner = [candidate, votes]
print("-------------------------")
print(f"Winner: {winner[0]}")
print("-------------------------")