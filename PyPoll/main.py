import csv
import os
#set path
file = os.path.join("Resources","election_data.csv")
# Initialize variables
total_votes = 0
candidates = {}
winner = ""
max_votes = 0

# Open the CSV file and loop through the rows
with open(file) as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        total_votes += 1
        candidate = row["Candidate"]

        if candidate not in candidates:
            candidates[candidate] = 1
        else:
            candidates[candidate] += 1

# prepare print analysis
output = "Election Results\n"
output += "-------------------------\n"
output += f"Total Votes: {total_votes}\n"
output += "-------------------------\n"

for candidate, votes in candidates.items():
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    if votes > max_votes:
        max_votes = votes
        winner = candidate

output += "-------------------------\n"
output += f"Winner: {winner}\n"
output += "-------------------------\n"

# Print the analysis to the terminal
print(output)

# Export a text file 
with open("election_results.txt", "w") as txtfile:
    txtfile.write(output)
