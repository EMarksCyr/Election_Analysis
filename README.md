# Election_Analysis

## Overview of Election Audit
Tom, a colorado board of elections employee, requested assistance with an election audit of the tabulated results for the U.S. congressional precinct of Colorado. 
We have been asked to perform the following tasks:
  - Calculate the total number of votes cast.
  - Get a complete list of all candidates that received votes. 
  - Calculate the total number of votes that each candidate received.
  - Calculate the percentage of votes that each candidate won.
  - Determine the winner of the election based on popular vote
  
This task has previously been done on excel; however, we have been asked to write a python script for the process. If successful, it can be re-used to audit other congressional districts, senatorial districts and local elections. Github was used to allow the client to access our work intermittently throughout the code-writing process.

The data has come in the form of a .csv file containing votes (inputted via a combination of mail-in ballots, punch cards and DRE vote-counting machines), voter IDs and counties. Results are to be saved to a .txt file containing the outcomes of the analysis. This will be saved to election_results.txt

## Election-Audit Results
 - Total number of votes cast: 369,711
 - Number of votes, and percentage of total votes, per precinct:
 	- Jefferson: 10.5% (38,855)
	- Denver: 82.8% (306,055)
	- Arapahoe: 6.7% (24,801)
 - County with the largest number of votes: Denver
 - Number of votes, and percentage of total votes, per candidate:
	- Charles Casper Stockham: 23.0% (85,213)
	- Diana DeGette: 73.8% (272,892)
	- Raymon Anthony Doane: 3.1% (11,606)
 - Winning candidate summary:
	- Winner: Diana DeGette
	- Winning Vote Count: 272,892
	- Winning Percentage: 73.8%

## Election-Audit Summary
Due to the switch from Excel to Python, the client now has a script that may be re-used, with modifications, for other elections in the future. 

In order to re-use this code as it is, you only need to edit a small section of the script. This would be a very quick adjustment to make. This section of the code below assigns the relative path to your input data and output text file as variables that are referenced throughout the script.
```python
file_to_load = os.path.join("Resources", "election_results.csv")
file_to_save = os.path.join("Resources", "election_results.txt")
```

This means that you only need to edit these two paths to your new data file and the output file location and name that you want, and the rest of the code will automatically reference them when performing the analysis.

While it's easy to re-use the code as-is, this can also be adjusted with relative ease to analyze other factors of interest.
The script contains for-loops that iterate through a .csv file and tabulate the number of votes per candidate or per county. These loops follow the same structure and can be efficiently modified to tabulate voter turnout for additional criteria such as demographics. 

For example, 
```python
county_list = []
county_votes = {}
for row in reader:
	county_name = row[1]
	if county_name not in county_list:
		county_list.append(county_name)
		county_votes[county_name] = 0
	county_votes[county_name] += 1
 ```

The code above creates a list to hold each county's names and a dictionary to hold the number of votes per county. It then iterates through the data file and fills the list with each new county name it encounters in the file and adds up the number of votes within that county.  This could be modified to tabulate the number of votes specific to any factor relevant to a given election, be that age, gender, or the like, as long as there is a column containing this information in the data file. If the election in question is a local election, this could be modified to tabulate results per ward instead of per county. This is just one example of how you can apply this code to any number of voter categories.

Aside from re-purposing, this code can also be modified to calculate the percent of voter turnout amongst the categories of interest. 

```python
total_votes = 0
for row in reader:        
	total_votes = total_votes + 1
```

The code above adds up the total number of votes cast as it iterates through the file while the county tabulator previously mentioned tallies up the number of votes per county. The same mechanic could be repurposed if information about the non-voting population was included from census data.  If the data file being referenced contained information for the entire population within each county and a column for whether they voted or not (e.g., voter = 1, non-voter = 2), both the totals for the overall population and voting population could be calculated and compared in a similar manner. A dictionary containing each category (e.g., county), the total population and total voting population for that category could be used to store the data. Yhen the for loop below could be adjusted to calculate voter turnout per category. 

```python
for candidate_name in candidate_votes:
	votes = candidate_votes.get(candidate_name)
	vote_percentage = float(votes) / float(total_votes) * 100
	candidate_results = (
		f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
```

In summary, this code has effectively delivered the audit requirements and is highly adjustable and ideal for re-use across a variety of election-audits. The code is organized so that it is easy to reassign the data file and output text file or to repurpose its components to tabulate results from different factors.


 ## Resources
  - Data source:election_results.csv
  - Software: Python 3.6.1, Visual Studio Code, 1.38.1
