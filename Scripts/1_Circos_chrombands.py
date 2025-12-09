#This script is meant to take a barcode input file and define all the tissues to be plotted and all the barcodes present in those tissues as colored bands. 

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
		print('chr - ',i,' ', i,' ','0',' ','100',' ','grey_a5')
print('#')
for i in chrome:
	if chrome[i][0]=='LymphNodes':
		print('chr - ',i,' ', i,' ','0',' ','100',' ','grey_a5')
print('#')
for i in chrome:
	if chrome[i][0]=='ExtraPulmonary':
		print('chr - ',i,' ', i,' ','0',' ','100',' ','grey_a5')
print('#')
print('#')

barcodes={}

for line in open(sys.argv[1]):  # opens files line by line
    line = line.strip('\r\n')
    split= line.split('\t')         #splits columns by tabs
    num_barcode=len(split)-5 #number of columns minus 5 is the # of unique barcodes
    if split[0] != 'Sample #':
    	tissue=split[3] #sample name-will be chrom name
    	desig=split[4] #if tissue is lung, other thoracic, or extrapulmonary
    	band_start=1
    	counter=0
    	for x in range(5,len(split)):
    		if split[x].isdigit(): #if there is a barcode
    			counter = counter+1
    			barcode_num= x-4 #barcode number, starting with 1
    			color = 'chr'+str(barcode_num)
    			tis_bc_id = tissue + '_BC'+str(barcode_num)
    			if counter == 1:
    				band_start = 0
    				band_end = band_start + int(split[x])
    				barcodes[tis_bc_id]=[barcode_num,tissue,band_start,band_end,color]
    				band_start = band_end +1
    			if counter > 1:
    				band_end = band_start + int(split[x]) -1 #so end of each band increases by column
    				barcodes[tis_bc_id]=[barcode_num,tissue,band_start,band_end,color]
    				band_start = band_end + 1
    			
    			

#print out the list of bands

for i in barcodes:
	print('band',' ',barcodes[i][1],' ',barcodes[i][0],' ','band1',' ',barcodes[i][2],' ',barcodes[i][3],' ',barcodes[i][4])   	
    	