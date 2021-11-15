# ElectionAnalysis

## Project Overview
- This project analysis is for assisting Tom, A Colorado Board of Elections employee with the election audit of a recent local congressional election.
- The following are the task which has been performed based on the election data provided.

    1. The Total number of votes.
    2. List of counties.
    3. Total number of votes and percentage of total votes for each county.
    4. Largest County Turnout
    5. List of candidates.
    6. Total number of votes and Percentage of total votes for each candidate. 
    7. Winner of the election based on popular vote.

## Resources
- Data source: election_result.csv
- Software : Python 3.7 , Visual Studio Code 1.62.2

## Results

## Total Number of Votes cast 
- Total number of votes is calculated by reading each row in the CVS file and incrementing the Total count variable every time a row is read.
- Below is the code written for counting rows (votes) in a CSV file

![1](https://user-images.githubusercontent.com/92698873/141674875-1aacd22d-14e1-452f-aa9f-2108137204b5.png)

-From the analysis the total number of votes is 369,711

![2](https://user-images.githubusercontent.com/92698873/141713450-0834feca-0dbf-4702-b240-d626c7a533a8.png)

## The number of votes and the percentage of total votes for each county in the precinct.

- The list of counties is got from the file. The county column is in the second column that has one as an index.

![Screenshot 2021-11-14 174304](https://user-images.githubusercontent.com/92698873/141714613-9a8a6848-445c-4a06-af66-d9f2795b7217.png)

![Capture](https://user-images.githubusercontent.com/92698873/141710159-f5b69ca2-4b78-4310-a710-7f31fe764766.PNG)

- County Name is added to the county list (if it is not in the list) and also number of votes for each county are added in dictionary.

![3](https://user-images.githubusercontent.com/92698873/141712679-a32222f6-ea0d-4643-b9c3-103f025b99cb.png)

![4](https://user-images.githubusercontent.com/92698873/141712968-65154b3c-9b7d-4a62-90bf-1a3a3d9a4c89.png)

- To calculate the percentage for each county - the County and number of votes for each county are got from the dictionary.
- Below is code for calculating the percentage :

![6](https://user-images.githubusercontent.com/92698873/141713103-6dc35abb-28b9-4191-aedd-1ed0c53fb25c.png)
- Below is the result of the list of counties, their total votes, and the percentage of total votes.

![7](https://user-images.githubusercontent.com/92698873/141713917-be5688b2-b7eb-4e3c-a953-eceab11c0cfd.png)

## County with the largest number of votes
- Each and every county in the list is being checked if its greater than the other. Below is the code for getting the largest number.

![9](https://user-images.githubusercontent.com/92698873/141715057-c2f11bdc-3da2-465f-9c9a-d568c5edbbf9.png)

- It turns out that Denver has the highest votes with total of 306,055 and 82.8% of total votes.

![8](https://user-images.githubusercontent.com/92698873/141715065-66013d8b-f42d-48ec-b09f-b6ddf64ac6e9.png)

## The number of votes and the percentage of the total votes each candidate received.
- The list of Candidates is read from the file. The candidate column is in the third column that has two as an index.

![12](https://user-images.githubusercontent.com/92698873/141716311-68b938a8-6452-4d21-be95-b0c6fe822733.png)

- Candidates Name is added to the Candidates list (if it is not in the list) and also number of votes for each Candidates are added in dictionary.

![11](https://user-images.githubusercontent.com/92698873/141716542-2c509e47-7a12-44cb-b211-e8e34cd41c7e.png)

- To calculate the percentage for each Candidates - the Candidates and number of votes for each Candidates are got from the dictionary.

![13](https://user-images.githubusercontent.com/92698873/141716592-a2796612-2906-490a-8064-5b07e66ef699.png)

- Below is the result of the list of Candidates, their total votes, and the percentage of total votes.

![10](https://user-images.githubusercontent.com/92698873/141716815-389fac14-4b45-495c-950c-209daabfe448.png)

 


## Summary
The analysis of the election show that :
- There were 369,711 votes cast in the election.
- The Candidates were :
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The Candidates results were :
    - Charles Casper Stockham recived 23.0 % of the vote and 85,213 number of votes.
    - Diana DeGette recived 73.8 % of the vote and 272,892 number of votes.
    - Raymon Anthony Doane recived 3.1 % of the vote and 11,606 number of votes.


