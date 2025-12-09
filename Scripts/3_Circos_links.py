#This script is meant to take a barcode input file and define the barcodes that are shared between tissues (so-called links). The output file will be a tab-delimited file compatible with the links input needed by the Circos file to draw ribbon connections.

#Input argv[1] is tab delimited NHP barcoding file form 1 NHP
#Input file has the following columns: Sample#, Monkey ID, Group, Sample Name, Designation, then all further columns represent different barcodes 
#Input file has every row being a different tissue


import sys

#create dictionary of tissue samples for creating chromosome list

barcodes={}

for line in open(sys.argv[1]):  # opens files line by line
    line = line.strip('\r\n')
    split= line.split('\t')         #splits columns by tabs
    num_barcode=len(split)-5 #number of columns minus 5 is the # of unique barcodes
    if split[0] != 'Sample #':
    	tissue=split[3] #sample name-will be chrom name
    	desig=split[4] #if tissue is lung, other thoracic, or extrapulmonary
    	band_start=0
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
    				barcodes[tis_bc_id]=[barcode_num,tissue,band_start,band_end,color,desig]
    				band_start = band_end +1
    			if counter > 1:
    				band_end = band_start + int(split[x]) -1 #so end of each band increases by column
    				barcodes[tis_bc_id]=[barcode_num,tissue,band_start,band_end,color,desig]
    				band_start = band_end + 1
    	

#create dictionary of all potential links, including redundant and reciprocal links

links={}

counter=0
for i in barcodes:
	start_desig=barcodes[i][5]
	start_tissue=barcodes[i][1]
	color=barcodes[i][4]
	for x in barcodes:
		if color == barcodes[x][4]: #if color/BC of this lung sample equal any of another sample
			if start_tissue != barcodes[x][1]: #so you don't report a barcode for self band
				counter = counter +1
				linkID = i + "_link"+str(counter)
				#cols: start tissue, start pos, end pos, end tissue, start pos, end pos, BC (as number),type of tissue
				links[linkID]=[start_tissue,barcodes[i][2],barcodes[i][3],barcodes[x][1],barcodes[x][2],barcodes[x][3],color,start_desig]


#parse list of links for those that are unique, with priority given to those originating from lung tissue

unique_links={}				

BClist=[]
BCdict={}

#create a register of all unique BCs and entries for their links

for i in links:
	if links[i][7] == 'Lung':
		if links[i][6] not in BClist: #first time you see a BC
			BClist.append(links[i][6])
			BCs=links[i][6]
			BCdict[BCs]=[links[i][0],links[i][3]] #now dict called by chromX & has links of tissue attached 
			unique_links[i]=[links[i][0],links[i][1],links[i][2],links[i][3],links[i][4],links[i][5],links[i][6],links[i][7]]
	
for i in links:
	if links[i][7] == 'Thoracic':
		if links[i][6] not in BClist: #first time you see a BC
			BClist.append(links[i][6])
			BCs=links[i][6]
			BCdict[BCs]=[links[i][0],links[i][3]] #now dict called by chromX & has links of tissue attached
			unique_links[i]=[links[i][0],links[i][1],links[i][2],links[i][3],links[i][4],links[i][5],links[i][6],links[i][7]]
	
for i in links:
	if links[i][7] == 'Extra':
		if links[i][6] not in BClist: #first time you see a BC
			BClist.append(links[i][6])
			BCs=links[i][6]
			BCdict[BCs]=[links[i][0],links[i][3]] #now dict called by chromX & has links of tissue attached 
			unique_links[i]=[links[i][0],links[i][1],links[i][2],links[i][3],links[i][4],links[i][5],links[i][6],links[i][7]]

# now to only put in links that are non-redundant


for i in links:
	if links[i][7] == 'Lung':
		BC=links[i][6]
		if links[i][0] not in BCdict[BC] or links[i][3] not in BCdict[BC]:
			BCdict[BC].append(links[i][0])
			BCdict[BC].append(links[i][3])
			unique_links[i]=[links[i][0],links[i][1],links[i][2],links[i][3],links[i][4],links[i][5],links[i][6],links[i][7]]
	
for i in links:
	if links[i][7] == 'Thoracic':
		BC=links[i][6]
		if links[i][0] not in BCdict[BC] or links[i][3] not in BCdict[BC]:
			BCdict[BC].append(links[i][0])
			BCdict[BC].append(links[i][3])
			unique_links[i]=[links[i][0],links[i][1],links[i][2],links[i][3],links[i][4],links[i][5],links[i][6],links[i][7]]
	
for i in links:
	if links[i][7] == 'Extra':
		BC=links[i][6]
		if links[i][0] not in BCdict[BC] or links[i][3] not in BCdict[BC]:
			BCdict[BC].append(links[i][0])
			BCdict[BC].append(links[i][3])
			unique_links[i]=[links[i][0],links[i][1],links[i][2],links[i][3],links[i][4],links[i][5],links[i][6],links[i][7]]

#print out the list of unique links

unique_sites = unique_links.keys()
sorted(unique_sites)

for i in unique_sites:
	print(unique_links[i][0],'\t',unique_links[i][1],'\t',unique_links[i][2],'\t',unique_links[i][3],'\t',unique_links[i][4],'\t',unique_links[i][5])
    	