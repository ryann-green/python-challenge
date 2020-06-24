#import our contents
import os
import csv
import sys

#work to the csv file that we need to extract to work on this program
csv_path= os.path.join("Resources","budget_data.csv")

original_stdout = sys.stdout # Save a reference to the original standard output
with open('Analysis/ budget_analysis.txt', 'w') as f: #open the text file and path we want to save stuff in
        sys.stdout = f # Change the standard output to the file we created.

        #open the csv_path as a csv file
        with open(csv_path) as csvfile:

                #read the contents of the csvfile and split by a comma
                csv_reader = csv.reader(csvfile, delimiter=",")

                #print the csv_reader
                #print(csv_reader)
                
                csv_header = next(csv_reader) #eliminate the header row
                #print the header row
                #print(csv_header)

                #identify our variables to hold values
                total_months=0
                net_profit_loss=0
                avg_profit_loss=0
                g_increase = 0
                g_increase_month = ""
                g_decrease = 0
                g_decrease_month=""
                current_change=0
                previous_number=0

                avg_list=[]
                avg_list_month=[]

                new_array ={"Month":avg_list_month,"Average p/l":avg_list}
                
                #begin loop through csv file
                for row in csv_reader:
                
                        total_months +=1 #continue adding to the total # of months for each row
                        
                        net_profit_loss+=int(row[1]) #add to the total net ptofit/loss for each row depending on the value in the second column
                
                        current_change=int(row[1])-previous_number #find subtract the previous number from the current value and make it the current change
                
                        avg_list.append(current_change)#append the current change value to the csv list as an additional column

                        if current_change > g_increase: #check to see if the current change is greater than the greatest increase, if so..
                                g_increase = current_change #replace the greatest change with the current change
                                g_increase_month = row[0] #place the current month as the greatest increase month
                        elif current_change < g_decrease: #if the current change isn't greater than the greatest increase, let's check to see if it's lower than the lowest increase. if so...
                                g_decrease = current_change #replace the lowest change with the current change
                                g_decrease_month = row[0] #place the current month as the lowest increase month

                        previous_number=int(row[1])#make the current row the previous number before ending the for loop and moving to the next row
                
                #print(avg_list)#print the average list
                avg_profit_loss=(sum(avg_list[1:])/len(avg_list[1:]))
                #g_increase = max(avg_list)
                #g_decrease = min(avg_list)
                print("Financial Analysis")
                print("--------------------------------------")

                #print the results
                print("Total Months: "+str(total_months))
                print("Total: $"+str(net_profit_loss))
                print("Average change: "+str(round(avg_profit_loss,2)))
                print("Greatest increase in Profits: "+g_increase_month+" ($"+str(g_increase)+")")
                print("Greatest decrease in Profits: "+g_decrease_month+" ($"+str(g_decrease)+")")
                
        sys.stdout = original_stdout # Reset the standard output to its original value

