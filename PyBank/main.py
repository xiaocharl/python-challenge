import os
import csv


budgetpath=os.path.join('Resources','budget_data.csv')
# define initial parameters
monthnum=0
total=0
change_row=[]
month=[]
profit=867884
with open(budgetpath,'r') as csvfile:
	#skip header
	csvreader= csv.reader(csvfile,delimiter=",")
	next(csvreader)
	for row in csvreader:
		#calculate total profit
		total = total + int(row[1])
		#calculate total month
		monthnum=monthnum+1
		# create month 
		month.append(row[0])

	# calculate change profit value
		change=int(row[1])-profit
		# add change profit
		change_row.append(change)
		profit=int(row[1])
		
	#find average and max increase, decrease value
	average=round(sum(change_row)/(int(monthnum)-1),2)
	maxincrease=max(change_row)
	maxdecrease=min(change_row)
	#find row number
	row_maxincrease=change_row.index(int(maxincrease))
	row_maxdecrease=change_row.index(int(maxdecrease))

	#print Results
	print('Finicial Analysis')
	print("----------------------------")
	print('Total Month: '+str(monthnum))
	print('Total: ' + str(total))
	print('Average Change: $'+str(average))
	print('Greatest Increase in Profits:'+str(month[row_maxincrease])+'($'+str(maxincrease)+')')
	print('Greatest Decrease in Profits:'+str(month[row_maxdecrease])+'($'+str(maxdecrease)+')')
	


	# out put csv file into analysis folder
outputpath =os.path.join("analysis","result.csv")
with open(outputpath,"w",newline="") as datafile:
	# Create variable
	writer=csv.writer(datafile)

	# define each line
	
	line1=(["Finicial Analysis","Total Month:","Total: $","Average Change", "Greatest Increase in Profits:","Greatest Decrease in Profits:"])
	line2=(["",str(monthnum),str(total),str(average),str(month[row_maxincrease]),str(month[row_maxdecrease])])
	line3=(["","","","",str(maxincrease),str(maxdecrease)])
	# zip into a data file

	finalresult=zip(line1,line2,line3)
	writer.writerows(finalresult)
	