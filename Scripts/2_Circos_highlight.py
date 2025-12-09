#This script is meant to take a barcode input file and color all the tissues to be plotted by their anatomical compartment. 

#Input argv[1] is tab delimited NHP barcoding file form 1 NHP
#Input file has the following columns: Sample#, Monkey ID, Group, Sample Name, Designation, then all further columns represent different barcodes 
#Input file has every row being a different tissue

import sys

#create dictionary of tissue samples for creating chromosome list

chrome={}

for line in open(sys.argv[1]):  # opens files line by line
    line = line.strip('\r\n')
    split= line.split('\t')         #splits columns by tabs
    if split[0] != 'Sample #':
    	tissue=split[3] #sample name-will be chrom name
    	desig=split[4] #if tissue is lung, other thoracic, or extrapulmonary
    	chrome[tissue]=[desig]


#print out the list of chromosomes

for i in chrome:
	if chrome[i][0]=='Lung':
		print(i,' ','0',' ','100',' ','fill_color=red')
print('#')
for i in chrome:
	if chrome[i][0]=='LymphNodes':
		print(i,' ','0',' ','100',' ','fill_color=blue')
print('#')
for i in chrome:
	if chrome[i][0]=='ExtraPulmonary':
		print(i,' ','0',' ','100',' ','fill_color=green')