import os
import csv

#here, i give the paht where is the file.
dataopen=os.path.join("C:/Users/sebat/ClassRepository/python-challenge/PyBank/Resources/budget_data.csv")

#Now, i create some variable to calculate  
#this variable is to calculate the total month.
date_count=0
#this list is to save every changes
list_change=[]
list_month=[]
#this variable is to calculate the total changes in the incomes
total_change=0
#this is to calculate every change every month
change=0
#this variable is to calculate the total net income.
total_net_income=0

#with code, i am opening the csv file
with open(dataopen) as csvfile:
    #with this, i am saying that i dont want to considerer the first row, because it doesnt contains numbers
    next(csvfile)
    csvreader=csv.reader(csvfile,delimiter=",")
    
   #here, i start to read every row of the csv file.    
    for row in csvreader:
        #count every month
        date_count+=1
        #here i am adding up every income or losses per month
        total_net_income=total_net_income+float(row[1])
        
        #here, i am calculate the changes. i use "if" to the first row, i didnt calculate the change because i dont have nothing to compare, so i add "0" in the list.
        if len(list_change)!=0:
            #with this, i calculate the change, and then, i add to the list.
            change=round(int(-change+float(row[1])),)
             
        list_change.append(float(change))
        list_month.append(row[0])

        #i save in this variable the last income.
        change=float(row[1])
    
    #this "print" is to see how is the list of changes
    #print(list_change)
    #print(list_month)

    #with this loop, i calculate the total changes, and then, i divide by total month and i get the average of changes.
    for x in list_change:
       total_change=total_change+float(x)

    average=round(total_change/(date_count-1),2)
    
    #with this, i see what is the month of the higher change and lower change.
    month_max=list_month[list_change.index(max(list_change))]
    month_min=list_month[list_change.index(min(list_change))]
    
    #this is to see what month is.
    print(month_max)
    print(month_min)
    
    #this print, is to see the result of the average of changes.
    #print(average)    

#here, i try to see the result before to write the final result inside of the text file 
print(f"Total Month: {date_count}")
print(f"Total: ${round(int(total_net_income),0)}")
print(f"Average Change:${float(average)}")
print(f"Greatest Increase in profits: {month_max} (${round(max(list_change),)})")
print(f"Greatest Decrease in profits: {month_min} (${round(min(list_change),)})")

#here, i am creating a new text file and write the result inside of it.
dataout=os.path.join("C:/Users/sebat/ClassRepository/python-challenge/PyBank/analysis/Analysis_Pybank.txt")
with open(dataout,'w',newline='') as csvfile:
    csvwriter=csv.writer(csvfile,delimiter=",")
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Total Month: {date_count}"])
    csvwriter.writerow([f"Total: ${round(int(total_net_income),0)}"])
    csvwriter.writerow([f"Average Change:${float(average)}"])
    csvwriter.writerow([f"Greatest Increase in profits: {month_max} (${round(max(list_change),)})"])
    csvwriter.writerow([f"Greatest Decrease in profits: {month_min} (${round(min(list_change),)})"])