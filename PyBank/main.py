import os
import csv

csvpath = os.path.join("..","..","..","..","..","..","Desktop","GTATL201908DATA3",
                       "02 - Homework","03-Python","Instructions","PyBank","Resources",
                       "budget_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    count = 0
    average_l = []
    profit_l = []
    full_l = []
    f = open("PyBank_results.txt","w")
    
    for row in csvreader:
        profit_l.append(int(row[1]))
        average_l.append(int(row[1]))
        full_l.append(row[0])
        count += 1

    print("Financial Analysis")
    print("------------------")
    print("Total Months: {}".format(count))
    print("Total: ${}".format(sum(profit_l)))
    
print("Financial Analysis", file=f)
print("------------------", file=f)
print("Total Months: {}".format(count), file=f)
print("Total: ${}".format(sum(profit_l)), file=f)

def average(num1_l,num2_l):
    average_change=([j-i for i,j in zip(num1_l,num2_l)])
    maximum = int(max(average_change))
    minimum = int(min(average_change))
    
    for k in average_change:
        if k == maximum:
            locate = (average_change.index(k)+1)
            
    for m in average_change:
        if m == minimum:
            locate2 = (average_change.index(m)+1)
            
    print("Average Change: ${}".format(round(sum(average_change)/(count-1),2)))
    print("Greatest Increase in Profits: {} (${})".format(full_l[locate],maximum))
    print("Greatest Decrease in Profits: {} (${})".format(full_l[locate2],minimum))
    
    print("Average Change: ${}".format(round(sum(average_change)/(count-1),2)), file=f)
    print("Greatest Increase in Profits: {} (${})".format(full_l[locate],maximum), file=f)
    print("Greatest Decrease in Profits: {} (${})".format(full_l[locate2],minimum), file=f)
    

    return  
    
profit_l.pop()
average_l.pop(-86)

average(profit_l,average_l)
f.close()