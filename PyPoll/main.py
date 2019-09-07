# import os and csv modules
import os
import csv
import operator

election_data = os.path.join('..', 'PyPoll', 'Election_Data.csv')

with open(election_data, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    total_votes = 0
    Khan_total = 0
    Correy_total = 0
    Li_total = 0
    OTooley_total = 0
    unduplicated_candidates = set()
    
    # calculate total number of votes cast

    for row in csvreader:
        total_votes = total_votes + 1

    # generate list unique list of candidates
        unduplicated_candidates.add(row[2]) 

    # number of votes each candidate won

        # create a conditional that looks for an index with each candidate name 
        if row[2] == "Khan":
            # increment vote count
            Khan_total = Khan_total +1
        
        elif row[2] == "Correy":
            Correy_total = Correy_total +1

        elif row[2] == "Li":
            Li_total = Li_total +1

        elif row[2] == "O'Tooley":
            OTooley_total = OTooley_total +1

    # percentage of votes each candidate won
        Khan_precent = (Khan_total / total_votes) * 100
        Correy_percent = (Correy_total / total_votes) * 100
        Li_percent = (Li_total / total_votes) * 100
        OTooley_percent = (OTooley_total / total_votes) * 100

    # identify the winner of the election
        election_dict = {
                        "Khan": [Khan_precent, Khan_total],
                        "Correy": [Correy_percent, Correy_total],
                        "Li": [Li_percent, Li_total],
                        "O'Tooley": [OTooley_percent, OTooley_total]
                        }
        winner = max(election_dict.items(), key=operator.itemgetter(1))[0]
 
    #  print election results to terminal  

    print("Election Results\n")
    print("---------------------------------------------------\n")
    print(f"Total Votes: {total_votes}\n")
    print("---------------------------------------------------\n")
    print(f'Khan: {Khan_precent:.3f}% {Khan_total}\n')
    print(f'Correy: {Correy_percent:.3f}% {Correy_total}\n')
    print(f'Li: {Li_percent:.3f}% {Li_total}\n')
    print(f"O'Tooley: {OTooley_percent:.3f}% {OTooley_total}\n")
    print("---------------------------------------------------\n")
    print(f'Winner: {winner}\n')

    #  print election results to new txt file  

    file = open("PyPollResults.txt", "w+")
    
    file.write("Election Results\n")
    file.write("---------------------------------------------------\n")
    file.write(f'Total Votes: {total_votes}\n')
    file.write("---------------------------------------------------\n")
    file.write(f'Khan: {Khan_precent:.3f}% ({Khan_total})\n')
    file.write(f'Correy: {Correy_percent:.3f}% ({Correy_total})\n')
    file.write(f'Li: {Li_percent:.3f}% ({Li_total})\n')
    file.write(f"O'Tooley: {OTooley_percent:.3f}% ({OTooley_total})\n")
    file.write("---------------------------------------------------\n")
    file.write(f'Winner: {winner}\n')
