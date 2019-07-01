import os 
import csv

entire_candidate_list = []
unique_candidate_list = []



csvpath = os.path.join('election_data.csv')
with open(csvpath, newline='') as csvfile:
    polls_file = csv.reader(csvfile, delimiter = ",")

#The total number of votes cast = 
#A complete list of candidates who received votes=
#The percentage of votes each candidate won =
#The total number of votes each candidate won=
#The winner of the election based on popular vote.=

   
   #created a list of all candidates
    for col in polls_file:
        entire_candidate_list.append(col[2])

    entire_candidate_list = entire_candidate_list[1:]
    
    #used len function to figure out how many votes were cast
    num_votes = len(entire_candidate_list)

    #used for loop to add unique values into my unique_candidate list

    for x in entire_candidate_list:
        if x not in unique_candidate_list:
            unique_candidate_list.append(x)


    #created a function that would tally the amount of times each candidate recieved a vote 
    def count_cand(entire_candidate_list, cand):
        count = 0 
        for values in entire_candidate_list:
            if (values == cand):
                count = count + 1 
        return count

    cand = "Khan"
    khan_count = count_cand(entire_candidate_list, cand)
    
    cand = "Correy"
    correy_count = count_cand(entire_candidate_list, cand)

    cand = "Li"
    li_count = count_cand(entire_candidate_list, cand)

    cand = "O'Tooley"
    otooley_count = count_cand(entire_candidate_list, cand)

    ### using basic math to find percentageof votes fro each candidate  
    percentage_khan = int((khan_count / num_votes)*100)
    percentage_correy = int((correy_count / num_votes)*100)
    percentage_li = int((li_count / num_votes)*100)
    Percentage_otooley = int((otooley_count / num_votes)*100)






print('ELECTION RESULTS')
print('----------------------')


print(f'Total Votes: {num_votes}')
print('----------------------')

print(f'Khan: {percentage_khan}% ({khan_count})')
print(f'Correy: {percentage_correy}% ({correy_count})')
print(f'Li: {percentage_li}% ({li_count})')
print(f"O'Tooley: {Percentage_otooley}% ({otooley_count})")
print('----------------------')

print(f'Winner: Khan')


