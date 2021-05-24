# import operating system module
import os

# Module for reading CSV files
import csv

# define path
csvpath=os.path.join('Resources','election_data.csv')
# Define initial vote
Khanvote=0
Correyvote=0
Livote=0
Tooleyvote=0
percent=[]
name=[]

# count vote use for loop
with open(csvpath,'r') as csvfile:
	csvreader =csv.reader(csvfile,delimiter=',')
	next(csvreader)
	for row in csvreader:
		if row[2]=="Khan":
			Khanvote=Khanvote+1
		elif row[2]=="Correy":
			Correyvote=Correyvote+1
		elif row[2]=="Li":
			Livote=Livote+1
		elif row[2]=="O'Tooley":
			Tooleyvote=Tooleyvote+1
# calculate total vote
	Totalvote=int(Khanvote)+int(Livote)+int(Correyvote)+int(Tooleyvote)
	
# Calculate percentage
	Khanpercent=(Khanvote/Totalvote)*100
# add name
	name.append("Khan")
	# add percent
	percent.append(Khanpercent)
	Correypercent=round((Correyvote/Totalvote)*100,4)
	name.append("Correy")
	percent.append(Correypercent)
	Lipercent=round((Livote/Totalvote)*100,4)
	name.append("Li")
	percent.append(Lipercent)
	Tooleypercent=round((Tooleyvote/Totalvote)*100,4)
	name.append("O'Tooley")
	percent.append(Tooleypercent)
	

# find highest vote
	index=percent.index(max(percent))
	
# use highest percent index to find winner
	winner=name[index]
	
# print results
	print("Election Results")
	print('------------------------')
	print('Khan: '+ "%.3f" % Khanpercent+'% (',str(Khanvote)+')')
	print('Correy: '+ "%.3f" % Correypercent+'% (',str(Correyvote)+')')
	print('Li: '+ "%.3f" % Lipercent+'% (',str(Livote)+')')
	print("O'Tooley: "+ "%.3f" % Tooleypercent+'% (',str(Tooleyvote)+')')
	print('------------------------')
	print('Winner: '+str(winner))
	print('------------------------')


#	# out put csv file into analysis folder
outputpath =os.path.join("analysis","result.csv")
with open(outputpath,"w",newline="") as datafile:
	# Create variable
	writer=csv.writer(datafile)

	# define each line
	
	line1=(["Elcetion Results ","Total Votes:","Khan:","Correy: ","Li: ", "O'Tooley:","Winner:"])
	line2=([" ",str(Totalvote),str(Khanpercent),str(Correypercent),str(Lipercent),str(Tooleypercent),str(winner)])
	line3=([" "," ", str(Khanvote),str(Correyvote),str(Livote),str(Tooleyvote)])
	# zip into a data file

	finalresult=zip(line1,line2,line3)
	writer.writerows(finalresult)
	