import os
import csv

csvpath = os.path.join("..","..","..","..","..","..","Desktop","GTATL201908DATA3",
                       "02 - Homework","03-Python","Instructions","PyPoll","Resources",
                       "election_data.csv")

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvfile)
    original_info_l = []
    count_khan = 0
    count_correy = 0
    count_li = 0
    count_otooley = 0
    f = open("PyPoll_results.txt","w")
    
    for row in csvreader:
        original_info_l.append(row[2])
        total_votes = len(original_info_l)
        
    print("Election Results")
    print("-------------------------")
    print("Total Votes: {}".format(total_votes))
    print("-------------------------")
    
    print("Election Results", file=f)
    print("-------------------------", file=f)
    print("Total Votes: {}".format(total_votes), file=f)
    print("-------------------------", file=f)
    
    for row in original_info_l:
        if row == "Khan":
            count_khan += 1
        if row == "Correy":
            count_correy +=1
        if row == "Li":
            count_li += 1
        if row == "O'Tooley":
            count_otooley += 1
    
    print("Khan: {}% ({})".format(round(((count_khan/total_votes)*100),3),count_khan))
    print("Correy: {}% ({})".format(round(((count_correy/total_votes)*100),3),count_correy))
    print("Li: {}% ({})".format(round(((count_li/total_votes)*100),3),count_li))
    print("O'Tooley: {}% ({})".format(round(((count_otooley/total_votes)*100),3),count_otooley))
    print("-------------------------")
    
    print("Khan: {}% ({})".format(round(((count_khan/total_votes)*100),3),count_khan), file=f)
    print("Correy: {}% ({})".format(round(((count_correy/total_votes)*100),3),count_correy), file=f)
    print("Li: {}% ({})".format(round(((count_li/total_votes)*100),3),count_li), file=f)
    print("O'Tooley: {}% ({})".format(round(((count_otooley/total_votes)*100),3),count_otooley), file=f)
    print("-------------------------", file=f)   
    
    if count_khan > count_correy | count_li | count_otooley:
        print("Winner: Khan")
        print("Winner: Khan", file=f)
    if count_correy > count_khan | count_li | count_otooley:
        print("Winner: Correy")
        print("Winner: Correy", file=f)
    if count_li > count_correy | count_khan | count_otooley:
        print("Winner: Li")
        print("Winner: Li", file=f)
    if count_otooley > count_correy | count_khan | count_li:
        print("Winner: O'Tooley")
        print("Winner: O'Tooley", file=f)
    print("-------------------------")
    print("-------------------------", file=f)
    f.close()
