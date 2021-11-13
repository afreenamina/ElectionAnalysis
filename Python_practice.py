# First ever Python Program
print("Hello World")

# Determine the data type of an empty string.
print(type(""))

calc_1=5 + 2 * 3
print("5 + 2 * 3 = " + str(calc_1))
par_1=(5 + 2) * 3
print("(5 + 2) * 3 = " +str(par_1))

calc_2=8 // 5 - 3
print("8 // 5 - 3 ="+str(calc_2))
par_2=(8 // 5) - 3
print("(8 // 5) - 3 = "+str(par_2))

calc_3=8 + 22 * 2 - 4
print("8 + 22 * 2 - 4 =" +str(calc_3))
par_3= 8 + (22 * (2 - 4))
print("8 + (22 * (2 - 4)) =" +str(par_3))

calc_4=16 - 3 / 2 + 7 - 1
print("16 - 3 / 2 + 7 - 1 = " + str(calc_4))
par_4=16 - 3 / (2 + 7) - 1
print("16 - 3 / (2 + 7) - 1 = " +str(par_4))

calc_5=3 ** 3 % 5
print("3 ** 3 % 5 =" + str(calc_5))
par_5=3 ** (3 % 5)
print("3 ** (3 % 5) = "+str(par_5))

calc_6=5 + 9 * 3 / 2 - 4
print("5 + 9 * 3 / 2 - 4 = " +str(calc_6))
par_6=5 + (9 * 3 / 2 - 4)
print("5 + (9 * 3 / 2 - 4) = " +str(par_6))
par_7=5 + (9 * 3 / (2 - 4))
print("5 + (9 * 3 / (2 - 4)) = " +str(par_7))


counties=[]
counties = ["Arapahoe","Denver","Jefferson"]
#1)Add El Paso to the second position in the list. 
counties.insert(1,"El Paso")
print(*counties)

#2)Remove Arapahoe from the list.
counties.pop(0) 
print(*counties)

#3)Make Denver the third item in the list, but keep Jefferson the second item in the list.   
counties[1]="Jefferson"
counties[2]="Denver"
print(*counties)

#4)Add Arapahoe to the list. 
counties.append("Arapahoe")
print(*counties)

#dictionary 
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
print(*counties_dict)
print(counties_dict['Arapahoe'])
#------------------------------------
#Voting
voting_data = []
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
print(*voting_data)
#find the length of dictionary
print(len(voting_data))

#1)Add the new county “El Paso” and its registered voters, 461149, to the second position in voting_data. 
voting_data.insert(1,{"county":"El Paso", "registered_voters": 461149})
print("The voting List after added El Paso is = " + str(voting_data))

#2)Remove “Arapahoe” and its registered voters from voting_data. 
voting_data.pop(0)
print("The Voting List after deleting “Arapahoe” is = " +str(voting_data))

#3)Make “Denver” and its registered voters the third item in voting_data, 
# but keep “Jefferson” and its registered voters as the second item.   
voting_data.pop(1)
voting_data.append({'county': 'Denver', 'registered_voters': 463353})
print("The Voting List after alteration is = " +str(voting_data))

#4)Add “Arapahoe” and its registered voters to voting_data.
voting_data.append({'county': 'Arapahoe', 'registered_voters': 422829})
print("The Voting List after adding  is Arapahoe= " +str(voting_data))
#============================

#calculates the percentage of votes a candidate receives in an election
#my_votes=int(input("How many votes did you get in election?"))
#total_votes=int(input("What is the total votes in the election? "))
#percentage_votes=(my_votes/total_votes)*100

#print("I received " + str(percentage_votes)+"% of the total votes.")

#=========================
#if Statment 
#using the if statement on our counties list to determine if the second 
#county in the list is Denver. If so, then we will print "Denver" to the screen.

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == "Denver":
    print(counties[1])

#if else statment
temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

#nested if else
print ("EXMAPLE OF NESTED IF ELSE STATEMENT")
score=int(input("what is your test score?"))

if score>=90:
    print("Your Grade is A")
else:
    if score>=80:
        print("Your Grade is B")
    else:
        if score>=70:
            print("Your Grade is C")
        else:
            if score>=60:
                print("Your Grade is D")
            else:
                print("Your Grade is F")

#nested elif

#score=int(input("what is your test score?"))

if score>=90:
    print("Your Grade is A")
elif score>=80:
    print("Your Grade is B")
elif score>=70:
    print("Your Grade is C")
elif score>=60:
    print("Your Grade is D")
else:
    print("Your Grade is F")


#Membership Operators
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

#Logical Operator
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

if "Arapahoe" in counties and "El Paso" not in counties:
   print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# Example of for loop
for county in counties:
    print(county)