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
#use with open() to open and read the file so you don't have to close it later
with open(file_to_load) as election_data:
  
    #to do: read and analyze data
    file_reader = csv.reader(election_data)
    
    #prints out the contents of the file, remember, this needs to be tabbed over from the with line
    headers = next(file_reader)
    print(headers)




# #Using the open() function with the "w" mode for writing, we can write the data to the new file_to_save, assign that to a variable names outfile
# with open(file_to_save, 'w') as txt_file:

#     #write  something in the outfile
#     txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")
#     #close the outfile
#     txt_file.close()


