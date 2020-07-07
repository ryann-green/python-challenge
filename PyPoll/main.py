
import os #import the contents
import csv
import sys

csv_path = os.path.join("Resources","election_data.csv") #find the election data csv
original_stdout = sys.stdout # Save a reference to the original standard output

with open(csv_path, 'r') as csvfile: #open the election data csv as a csvfile

    csv_reader = csv.reader(csvfile, delimiter=",") #read the file as a csvfile and split the columns by a delimiter of ","

    csv_header = next(csv_reader) #skip the header row
    candidate_list=["Khan","Correy","Li","O'Tooley"] #create a list of the candidates
    total_vote = 0 #start a variable for keeping the total number of votes
    highestvotes=0 #hold a value for the highest number of votes
    winner=[] #hold a name for the winner
    candidate_results=[]

    csv_list = list(csv_reader) #make the csv reader an iterable list

    for row in csv_list: #begin interation to count how many votes there are (1 row = 1 total vote)
        total_vote+=1
               
    print("Election Results")
    print("-----------------------------------------")
    print("Total Election Votes: "+str(total_vote)) #print the total # of votes
    print("-----------------------------------------")

    for candidate in candidate_list: #begin iteration through the candidate list 
        percentage_vote=0 #canidates begin with 0% of the percentage vote and 0 votes total until we run through the ballots
        cand_vote=0

        for row in csv_list: #begin checking ballots
                
            if row[2] == candidate: #if the candidate name on the ballot is equal to the name of the candidate list we are checking then...
                cand_vote+=1 #add 1 vote to the candidates running total, then go to the next row

        if cand_vote > highestvotes: #if the number of votes received for a candidate are higher than the highest number of votes then
            highestvotes=cand_vote #replace the highest number of votes with the candidate # of votes
            winner.append(candidate) #make the current candidate the winner 
            
        percentage_vote=float(cand_vote)/float(total_vote) #divide the candidates votes by the total number of votes to get the % of votes for the candidate
        print(candidate+": "+str(round(percentage_vote*100,3))+"% ("+(str(cand_vote))+")") #print the candidate name, percentage of votes, and the # of votes received
        candidate_results.append([candidate, str(round(percentage_vote*100,3))+"%",(str(cand_vote))])
    
    
        #with open('Analysis/ election_results.txt','w') as f: #open the text file and path we want to save stuff in
            #print(candidate+": "+str(round(percentage_vote*100,3))+"% ("+(str(cand_vote))+")") #print the candidate name, percentage of votes, and the # of votes received
    
    #go to the next candidate in the canditate list

    print("-----------------------------------------")
    print("Winner: " +(winner[0])) #print the winner
    print("-----------------------------------------")

#Write the results to the text file
with open('Analysis/ election_results.txt','w') as f: #open the text file and path we want to save stuff in

    f.write("-----------------------------------------")
    f.write("\n")
    f.write("Election Results")
    f.write("\n")
    f.write("-----------------------------------------")
    f.write("\n")
    f.write("Total Election Votes: "+str(total_vote)) #print the total # of votes
    f.write("\n")
    f.write("-----------------------------------------")
    f.write("\n")
    for r in candidate_results:
        f.write(str(r[0])+": "+str(r[1])+"% ("+str(r[2])+")")
        f.write("\n")
    f.write("-----------------------------------------")
    f.write("\n")
    f.write("Winner: " +(winner[0])) #print the winner
    f.write("\n")
    f.write("-----------------------------------------")

