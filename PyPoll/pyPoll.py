import csv
import os

candidateDict = {}

with open('election_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csvheader = next(csvreader)
    TotalVotes = 0

    for row in csvreader:
        TotalVotes = TotalVotes + 1
        if row[2] not in candidateDict:
                candidateDict[row[2]] = 0
        candidateDict[row[2]] +=1

mostVotes = 0
for key,val in candidateDict.items():
        if val > mostVotes:
                mostVotes = val
                winner = key
        percent = round(100*val/TotalVotes,3)
        print(f'{key}: {percent}% ({val})')

print(f'Winner: {winner}')

txtfile = open('output1.txt','w')
for key,val in candidateDict.items():
        if val > mostVotes:
                mostVotes = val
                winner = key
        percent = round(100*val/TotalVotes,3)
        txtfile.write(f'{key}: {percent}% ({val})\n')

txtfile.write(f'Winner: {winner}')
txtfile.close()



        



