#import csv file 
import os
import csv

#create path to file to read in
budget_data_csv = os.path.join('.', 'PyBank', 'budget_data.csv')                 

#set my variables
Month_Total = 0
Net_Total = 0
months = []
profit_loss = []
Total_Change = 0
Change_List = []

#read in the csv file to extract data
with open(budget_data_csv, newline="") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
    
#skip header row for data retrieval
        next(csv_reader)
        First_row = next(csv_reader)
        Month_Total += 1
        Net_Total += int(First_row[1])
        Previous = int(First_row[1])

        for row in csv_reader:
                months.append(row[0])
                Current = int(row[1])
                profit_loss.append(Current)
                change = Current - Previous
                Total_Change += change
                Change_List.append(change)
#calculate total months and total profit/loss

                Month_Total += 1
                Net_Total += Current
                Previous = Current
#calculate average changes in profit/losses over the entire time period - over every month
        Average_Change = Total_Change / (Month_Total-1)



#find the greatest increase (max) and greatest decrease (min)

        greatest_increase = max(Change_List)
        greatest_decrease = min(Change_List)
       


        

#print out summary
print('Financial Analysis')
print('- - - - - - - - - - - - ')
print('Total Months:', Month_Total)
print('Net Total:', Net_Total)
print('Average Change:', Average_Change)
print('Greatest Increase in Profits:', greatest_increase)
print('Greatest Decrease in Profits:', greatest_decrease)

with open("Financial_Analysis.txt", "w") as txt_file: 
        txt_file.write('Financial Analysis\n')
        txt_file.write('---------------------\n')
        txt_file.write('Total Months: ')
        txt_file.write(str(Month_Total))
        txt_file.write('\nNet Total: ')
        txt_file.write(str(Net_Total))
        txt_file.write('\nAverage Change: ')
        txt_file.write(str(Average_Change))
        txt_file.write('\nGreatest Increase in Profits: ')
        txt_file.write(str(greatest_increase))
        txt_file.write('\nGreatest Decrease in Profits: ')
        txt_file.write(str(greatest_decrease))

        


    

    

