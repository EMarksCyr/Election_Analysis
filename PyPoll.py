#What we need to achieve
#1. get the total number of votes overall
#2. create a list with the names of each candidate
#3. calculate the numbre of votes each candidate won
#4. calculate what percentage of the votes each candidate won
#5. determine the winner of the election 
import csv
import os

#If we are given/have the direct file path:
#file_to_load = 'Resources/election_results.csv
#with open(file_to_load) as election_data:


#If we are only given the inderect path
#Assign a variable for the file and load election_results.csv in mode 'r' to read the file, use >import os and >os.path.join if given an indirect path to a resource, otherwise use the direction path by manually typing it in from the folder you're in 
file_to_load = os.path.join("Resources", "election_results.csv")
#Assign a variable to file you want to write and save, this time I'll use a direct path, note that it share the election_results name but it's a seperate .txt file
file_to_save = 'Resources/election_results.txt'

#initialize the vote counter
total_votes = 0

#initialize the list candidate list
candidate_options = []

#declare the dictioniary made to hold candidate votes
candidate_votes = {}

#Initialize a winning candidate variable for their name and variables to tally their vote and calculate the percent
winning_candidate = " "
winning_count = 0
winning_percentage = 0

#use with open() to open and read the file so you don't have to close it later
with open(file_to_load) as election_data:
  
    #to do: read and analyze data
    file_reader = csv.reader(election_data)
    


    #Skips the header row
    headers = next(file_reader)
    #print this to confirm you've skipped the headers, if so, you should see the headers printed out
    #print(headers)

    #traverses the contents of the file, remember, this needs to be tabbed over from the with line
    for row in file_reader:
        #Add to the total vote count
        total_votes = total_votes + 1

        #Assign the candidate name to this variable
        candidate_name = row[2] 

        #Add the candidate name to list of candidates called candidate_options if it hasn't already been added
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #begin tracking that candidates vote count to store in the dictionary
            candidate_votes[candidate_name] = 0       
        #Add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
#save your results to the text file
#Using the open() function with the "w" mode for writing, we can write the data to the new file_to_save, assign that to a variable names outfile
with open(file_to_save, 'w') as txt_file:

    election_results = (
        f"\nElection Results\n"
        f"---------------------------\n"
        f"Total votes: {total_votes:,}\n"
        f"---------------------------\n")
    txt_file.write(election_results)

    #iterate though the candidate dictionary
    for candidate_name in candidate_votes:
        #retrieve the vote count for the candidate
        votes = candidate_votes[candidate_name]
        #calculate the percentage of votes, convert to floating point because they are int by default
        vote_percentage = float(votes) / float(total_votes) * 100
        #print in the .txt file the candidate name and percentage of votes, rounding the percentage to 2 decimal places
        txt_file.write(f"{candidate_name}: recieved {vote_percentage:.2f}% of the vote.\n")

        #determing the winning vote count and candidate
        #Determine if the votes is greater than the current winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            #if true then sett winning_count to = votes and winning percent to = vote percent
            winning_count = votes
            winning_percentage = vote_percentage
            #and set the winning_candidate to equal the current candidates name
            winning_candidate = candidate_name
    #print(f"The winning candidate is {winning_candidate}, with {winning_percentage:.2f}% of the vote")
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning vote percentage: {winning_percentage:.1f}%\n"
        f"Winning vote count: {winning_count:,}\n"
        f"-------------------------------\n")
    #save the summary to the .txt file
    txt_file.write(winning_candidate_summary)

txt_file.close()
