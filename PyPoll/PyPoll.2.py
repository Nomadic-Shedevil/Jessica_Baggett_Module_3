#import csv file 
import os
import csv

#create path to file to read in
election_data_csv = os.path.join('.', 'PyPoll', 'election_data.csv')

#set my variables
total_vote = 0
candidates = {}

#read in the csv file to extract data
with open(election_data_csv, newline="") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
#skip header row for data retrieval
    next(csv_reader)
    
    for row in csv_reader:
        total_vote += 1
        Candidate_rep = row[2]
      #adding each candidate to a list and totaling the votes associated with their names  
        if Candidate_rep in candidates:
           candidates[Candidate_rep] += 1

        else:
            candidates[Candidate_rep] = 1

    Winner = max(candidates, key = candidates.get)

        #checking to see that they are added to the list with their votes
        #for candidate in vote_per_candidate:
            #print(candidate)
    print("total_vote: ", total_vote)
    
    for Candidate_BooBoo in candidates:
        votes = candidates[Candidate_BooBoo]       
        percentage = (votes/total_vote)*100
    
        print(f"{Candidate_BooBoo}:{percentage:.3f}% ({votes})")
    print("Winner: ", Winner)

    #calculate percentage of votes per candidate
    #Voter_Portion = vote_per_candidate / (total_vote-1)
   
   #find winning candidate 
    #Winning_Candidate = max(vote_per_candidate)


#output file, make into a text file
with open("Election_Analysis.txt", "w") as txt_file:
    txt_file.write('Election Results\n')
    txt_file.write('-----------------------\n')
    txt_file.write('Total Votes: ')
    txt_file.write(str(total_vote))
    txt_file.write('\n--------------------------\n')
    for Candidate_BooBoo in candidates:
        votes = candidates[Candidate_BooBoo]       
        percentage = (votes/total_vote)*100
        txt_file.write(f"{Candidate_BooBoo}:{percentage:.3f}% ({votes})\n")
    txt_file.write('\n---------------------------\n')
    txt_file.write('Winner: ')
    txt_file.write(str(Winner))
 
