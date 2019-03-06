import csv
import os

data_list = []

with open('budget_data.csv') as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    monthOverMonth = 0
    prevMonth = 0
    greatestIncrease = 0
    greatestDecrease = 0
    totalMonths = 0
    totalPL = 0

    csvheader = next(csvreader)
    csvheader.append('Month over Month')

    for row in csvreader:
        
        
        data_list.append(row[0])
        data_list.append(row[1])
        
        # determine month over month change
        if prevMonth == 0:
            data_list.append(prevMonth)
        
        else:
            monthOverMonth = int(row[1]) - int(prevMonth)
            data_list.append(monthOverMonth)
        
        prevMonth = row[1]

        # determine positive change
        if monthOverMonth > 0 and monthOverMonth > greatestIncrease:
            greatestIncrease = monthOverMonth
            bestMonth = str(row[0])
        
        #determine negative change
        elif monthOverMonth < 0 and monthOverMonth < greatestDecrease:
            greatestDecrease = monthOverMonth
            worstMonth = str(row[0])


        data_list.append(greatestDecrease)
        data_list.append(greatestIncrease)
        totalMonths = totalMonths + 1
        totalPL = totalPL + int(row[1])

averageChange = totalPL/totalMonths

txtfile = open('output0.txt','w')
txtfile.write(f'Total Months = {totalMonths}\n')
txtfile.write(f'Total P/L = {totalPL}\n')
txtfile.write(f'Average Monthly Change = {averageChange}\n')
txtfile.write(f'Best Month over Month Increase = {bestMonth}, {greatestIncrease}\n')
txtfile.write(f'Worst Month over Month Decrease = {worstMonth}, {greatestDecrease}\n')
txtfile.close()

print(f'Total Months = {totalMonths}')
print(f'Total P/L = {totalPL}')
print(f'Average Monthly Change = {averageChange}')
print(f'Best Month over Month Increase = {bestMonth}, {greatestIncrease}')
print(f'Worst Month over Month Decrease = {worstMonth}, {greatestDecrease}')
