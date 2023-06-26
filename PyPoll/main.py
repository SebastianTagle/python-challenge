import os
import csv

#here, i give the paht where is the file.
dataopen=os.path.join("C:/Users/sebat/ClassRepository/python-challenge/PyPoll/Resources/election_data.csv")

#i create the variables to calculate the votes and the porcentages for each cadidates, to save the different candidates in a list.
candidates=[]
votes=[]
votes_percentaje=[]
total_votes=0

#with code, i am opening the csv file
with open(dataopen) as csvfile:
    
    #with this, i am saying that i dont want to considerer the first row, because it doesnt contains numbers
    next(csvfile)
    csvreader=csv.reader(csvfile,delimiter=",")
    
    #here, i start to read every row of the csv file. 
    for row in csvreader:
        #here, i am calculating the total amount of votes.
        total_votes=total_votes+1
        #with this if, i save every different candidates in the list. and then, i add the space for the votes and the porcentage votes for each different candidates in another list and 
        if not row[2] in candidates:
            candidates.append(str(row[2]))
            votes.append(0)
            votes_percentaje.append(0)
        #with this for, i am calculate the total vote for each candidates
        for x in candidates:
            if x==row[2]:
               votes[candidates.index(x)]= votes[candidates.index(x)]+1
    
    #with this, i am see the result of the variables.
    print(total_votes)       
    print(candidates)
    print(votes)
    #print(len(candidates))
        
    #with this for, i am calculate the percentage of the total vote for each candidates
    for x in range(len(candidates)):
        votes_percentaje[x]=votes[x]/total_votes

    #with this, i am see the result of the variables.
    print(votes_percentaje)

#here i am calculating what candidate have more votes
max_votes= max(votes_percentaje)
max_index= votes_percentaje.index(max_votes)

#here, i try to see the result before to write the final result inside of the text file 
print(["Election Results"])
print(["-------------------------------------------------"])
print([f"Total Votes: {total_votes}"])
print(["-------------------------------------------------"])
for x in range(len(candidates)):
    print([f"{candidates[x]} : {round(votes_percentaje[x]*100,3)} % ({votes[x]})"])

print(["-------------------------------------------------"])
print([f"Winner: {candidates[max_index]}"])
print(["-------------------------------------------------"])

#here, i am creating a new text file and write the result inside of it.
dataout=os.path.join("C:/Users/sebat/ClassRepository/python-challenge/PyPoll/analysis/Analysis_PyPoll.txt")
with open(dataout,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------------------------------"])
    for x in range(len(candidates)):
        csvwriter.writerow([f"{candidates[x]} : {round(votes_percentaje[x]*100,3)}% ({votes[x]})"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Winner: {candidates[max_index]}"])
    csvwriter.writerow(["-------------------------------------------------"])