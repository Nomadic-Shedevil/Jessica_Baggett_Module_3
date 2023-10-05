#import csv file 
import os
import csv

#create path to file to read in
election_data_csv = os.path.join('.', 'PyPoll', 'election_data.csv')

#set my variables
total_vote = 0
votes = []
candidates = []
candidate_votes = []

#read in the csv file to extract data
with open(election_data_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
#skip header row for data retrieval
    next(csv_reader)
    First_row = next(csv_reader)
    total_vote += 1
    Candidate = First_row[2]
    Previous_Canditate = First_row[2]
    
    for row in csv_reader:
      #adding each candidate to a list and totaling the votes associated with their names  
        if Candidate != Previous_Canditate:
            votes.append(total_vote)
            candidates.append(Candidate)
            vote_per_candidate = list(zip(candidates, votes))
        
        #checking to see that they are added to the list with their votes
        for candidate in vote_per_candidate:
            print(candidate)
    
    #calculate percentage of votes per candidate
    Voter_Portion = vote_per_candidate / (total_vote-1)
   
   #find winning candidate 
    Winning_Candidate = max(vote_per_candidate)

#print out summmary
print('Election Results')
print('-----------------------')
print('Total Votes:', total_vote)
print(candidate_votes)
print(Candidate, str(Voter_Portion), str(vote_per_candidate))
print('------------------------------')
print('Winner:', Winning_Candidate)

#output file, make into a text file
with open("Election_Results.txt", "w") as txt_file:
    txt_file.write('Election Results\n')
    txt_file.write('-----------------------\n')
    txt_file.write('Total Votes: ')
    txt_file.write(str(total_vote))
    txt_file.write('\n candidate_votes \n')
    txt_file.write(Candidate)
    txt_file.write(str(Voter_Portion))
    txt_file.write(str(vote_per_candidate))
    txt_file.write('\n ------------------------------\n')
    txt_file.write('Winner:')
    txt_file.write(str(Winning_Candidate))

    