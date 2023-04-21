# python-challenge
For PyBank

I made variables to keep track of the number of months in the dataset, the total profit/loss, the previous month's profit/loss, and a list to store the changes in profit/loss over time.
Then I used a with statement to open the CSV file, and a for loop to loop through each row in the file.
Inside the loop, I updated the variables to calculate the total months, total profit/loss, changes in profit/loss, and the greatest increase/decrease in profits.
Finally, I printed the financial analysis results to the console and exported them to a text file named results.txt.

For PyPoll

The first two lines of the script import the os and csv modules.
The third line uses the os.path.join() function to create a file path to the "election_data.csv" file located in a "Resources" directory.
I named some variables that will be used later: total_votes is set to 0, candidates is set to an empty dictionary, and winner and winner_votes are set to empty strings (since the winner hasn't been determined).
The next step is using a with statement to open the CSV file in read mode and creates a csv.reader object to loop through the rows in the file.
Skip first row (the headers) by using the next() function.
Then I loop over each row in the CSV file, counting the total_votes counter while adding the candidate's name to the candidates dictionary (if it doesn't already exist) and being paired with the corresponding vote count.
After all rows have been processed, the code creates a new file called "results.txt" in write mode and writes some header text to the file using the output_file.write() function.
It also prints the same header text to the console using the print() function.
Then I write the total number of votes to the output file and prints the same information to the console.
A for loop is used to loop through the items in the candidates dictionary.
For each candidate, the code calculates the percentage of the total vote they received, writes that information to the output file and prints the same information to the console. 
The loop also determines which candidate received the most votes and sets the winner and winner_votes variables accordingly.
Finally, the script writes the name of the winning candidate to the output file and prints the same information to the console, along with some footer text. The output_file is then closed.






