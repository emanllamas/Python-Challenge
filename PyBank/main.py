import os
import csv

##done just changing variable names

## created several empty lists 
total_num_months_list=[]
net_amount_list=[]
difference_list=[]


csvpath=os.path.join('budget_data.csv')

with open(csvpath,newline = '')as csvfile:
    csvreader = csv.reader(csvfile,delimiter = ",")
    
    # added the corresponding values to both empty lists, excluding the first value which is a header.
    for col in csvreader:
        total_num_months_list.append(col[0])
        net_amount_list.append(col[1])
        
    total_num_months_list = total_num_months_list[1:]
    net_amount_list = net_amount_list[1:]
     
    # Turned the values in the amount list into integers in order to be able to get the sum.
    net_amount_list = [int(i) for i in net_amount_list]


    #created a for loop using the range function in order to get the difference of each value month by month. Appended it to my difference list. 
    for row in range(1,len(net_amount_list)):
        difference_nums = net_amount_list[row]-net_amount_list[row -1]
        difference_list.append(difference_nums)
    # Used difference list to get the average of changes in the profit/losses column 
    average_change = sum(difference_list)/len(difference_list)

    # used the min/max function to then figure out the index of both the greatest and smallest change.
    greatest_change_amount = max(difference_list)
    min_change_amount = min(difference_list)

    greatest_change_amount_date = str(total_num_months_list[difference_list.index(max(difference_list))])
    min_change_amount_date = str(total_num_months_list[difference_list.index(min(difference_list))])



total_num_months_list = (len(total_num_months_list))
sum_amount_list = (sum(net_amount_list))





print("FINANCIAL ANALYSIS")
print("------------------")
print(f'Total Months: {total_num_months_list}')
print(f'Total: ${sum_amount_list}')
print(f'Average Change: ${int(average_change)}')
print(f'Greatest Increase in Profit: {greatest_change_amount_date} (${greatest_change_amount}) ')
print(f'Greatest Decrease in Profits: {min_change_amount_date} (${min_change_amount})')






