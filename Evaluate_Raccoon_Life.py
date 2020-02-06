"""
Created on Friday Jan 31 2020
by Ankit Ghanghas

Evaluavting the Life of a Raccoon.

This code takes an experimental data file(text file) as input and outputs a text file printing the the crucial information summary about the name of the subject of experiment, its mean position, mean energy level, total distance travelled. The output file also contains a hourly record of position, sleep flag, behaviour mode and calculated distance travelled in the last hour. 
"""

import math
data=open("2008Male00006.txt",'r') # opens the file in read mode as data
lines=data.readlines() # reads all the lines in the data file as 'lines'
data.close() # close the file 'data'
data=[0]*len(lines) # creates list of zeros of size equal to the number of lines in the original data
for i in range(1,len(lines)-1): # loops across all the lines except first and last
	data[i]=lines[i].strip().split(",") # strips the data in lines of all the python elements and splits it using comma delimmiter
	data[i][3:6]=map(float,data[i][3:6]) # maps the data stored in certain columns as floats to the list 'data'
	data[i][8:15]=map(float,data[i][8:15])
data.pop(0) # removes the first entry in the list 'data'
data.pop(-1) # removes the last entry in the list 'data'
info=lines[-1].strip().split(",") # saves the information in the last line of the original data in a separate parameter
head=lines[0].strip().split(",") # saves the information in the first line of original data as separate header
dictofmap={head[i] : [row[i] for row in data]  for i in range(len(head))} # creates a dictionary with the elements in head as key and the data in list 'data' as corresponding values
"""
The function average_list(a) takes a list 'a' as argument and returns the average of the list
"""
def average_list(a):
	return sum(a)/len(a)

def cum_sum(a):
	"""
	the function cum_sum find the cummulative sum of elements in a list and returns a list with cummulative sum till that element
	"""
	c=[0]*len(a)
	sum=0
	for i in range(len(a)):
		sum=a[i]+sum
		c[i]=sum
	return c

def distance(X,Y):
	"""
	this function calculates the distance travelled when X and Y coordinates are provided as lists
	"""
#	X=dictofmap[' X']
#	Y=dictofmap[' Y']
	c=[0]*len(X)
	i=1
	while i<len(X):
		c[i]=math.sqrt((X[i]-X[i-1])**2 + (Y[i]-Y[i-1])**2)
		i+=1
	return c
dictofmap.update({'Distance':distance(dictofmap[' X'],dictofmap[' Y'])}) # updates the existing dictionary and adds distance data with 'Distance' as the key
header=['Raccoon name: George number  ' + str(dictofmap["George #"][0]) + '\n', 'Average location: ' + str(average_list(dictofmap[" X"])) + ", " + str(average_list(dictofmap[" Y"])) +'\n', 'Distance traveled: ' + str(cum_sum(dictofmap['Distance'])[-1])+ '\n', 'Average Energy Level: ' + str(average_list(dictofmap['Energy Level'])) + '\n','Raccoon End State: '+ info[0]+ '\n','\n'] # creates the header list to write in the profile
file=open("Georges_life.txt",'w') # opens the file "Georges_life.txt" in write mode
file.writelines(header) # writes the elements in the list header to the file
dictofmap={k:dictofmap[k] for k in ('Day','Time',' X',' Y',' Asleep','Behavior Mode', 'Distance') if k in dictofmap} # creates a smaller dictionary with only select columns of the original data.
for key in dictofmap.keys(): # loops over the keys in the dictionary and writes them in the file separated by a tab
	file.write(str(key) + '\t')
file.write('\n') # tells to start writing new lines in the next line
for i in range(len(dictofmap['Distance'])):# loops over the values in the dictionary and writes them seperated by a tab
	for value in dictofmap.values():
		file.write(str(value[i]) + '\t')
	file.write('\n')
file.close() # closes the file "Georges_life.txt"
