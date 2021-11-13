# While Loop
x = 0
while x <= 5:
    print(x)
    x = x + 1

# Iteration - Print each county from the counties dictionary using the keys() method.
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys():
    print(county)

for countyvalue in counties_dict.values():
    print(countyvalue)


#Print each county and registered voter form the counties dictionary so that the output looks like this:
for keycounty,valuecounty in counties_dict.items():
    print((keycounty)+" county has " +str(valuecounty)+ " registered voters")


# Example of retreive the values in dictionary
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print("Value is : " + str(value))


#How would you retrieve the number of registered voters from each dictionary
for county_dict in voting_data:
     print(county_dict['registered_voters'])


#Using F-Strings with Dictionaries
for keyfcounty,keyfvalue in counties_dict.items():
    print(f"{keyfcounty} county has {keyfvalue} registered voters.")


#Multiline F-Strings & Format Floating-Point Decimals
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
    #f"You received {candidate_votes:,} number of votes. "
    #f"The total number of votes in the election was {total_votes:,}. "
    #f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#SkillDrill - Format Floating-Point Decimals
for keyfcounty,keyfvalue in counties_dict.items():
    print(f"{keyfcounty} county has {keyfvalue:,} registered voters.")
print("----------------------------------")


#SkillDrill
for votingprint in voting_data:
    print(f"{votingprint['county']} county has {votingprint['registered_voters']:,} registered voters")

