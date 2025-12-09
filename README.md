# Instructions for generating Circos Plots

### Input barcoding file:

- The barcodes present in each tissue for each NHP were exported as
  tab-delimited text files with the following format (see input.txt
  files for as examples):

  - Column 1/sample_id: placeholder text sufficient (e.g., ‘NULL’)

  - Column 2/monkey_id: NHP designation (placeholder text sufficient)

  - Column 3/group: treatment condition (placeholder text sufficient)

  - Column 4/sample: tissue sample names that are read by the scripts
    (mandatory)

  - Column 5/designation: anatomic compartment mandatory (script expects
    exact match to either ‘Lung’, ‘LymphNodes’ or ‘ExtraPulmonary’)

  - Columns 6+ /a1, etc: Each column represents a different barcode and
    the numbers in each cell are the percent of all barcode reads in
    that tissue attributed to each specific barcode. Absence of barcodes
    are denoted as empty cells

### Python script usage general instructions

- Create folders for each NHP and using the input barcode file for each
  NHP (see above), run the following 4 scripts independently, generating
  individual output files.

- Create a Circos configuration file (e.g., ‘xxxx.conf’) for each NHP
  that points to the newly generated files (see Part C).

- Install Circos software and plot using Circos configuration file for
  each NHP. Manually update the configuration file to change coloring,
  sample ordering and formatting.

## A. Python scripts

<u>1_Circos_chrombands.py script:</u>

- This script identifies all ‘samples’ in the barcoding input file and
  creates a wedge for these tissues.

- Then, it identified the barcodes present in the tissues and creates
  color bands representing their prevlanece in that tissue (i.e.,
  between 1-100%)

- The barcodes that are shared between tissues are given the same color
  to represent dissemination (color is designated using Circos’ default
  chromosome coloring scheme (e.g. chr1, chr2, etc)).

- The output of this script is a file (blank space-delimited) required
  by Circos for plotting (i.e., ‘karyotype.txt’)

- The order of the samples in the karyotype file defines the order in
  which they are plotted by Circos.

### Example terminal code

`python3 1_Circos_chrombands.py input.txt > karyotype.txt`

<u>2_Circos_highlight.py script:</u>

- This script searches the ‘designation’ column in the input file for
  the anatomical compartment associated with each tissue

- The output of the script creates a tab-delimited file, where every
  sample to be plotted is given a color representing the anatomical
  compartment (Lung = red, LymphNode=blue; ExtraPulmonary=green).

- The output of this script (i.e., ‘highlight.txt’) is a blank
  space-delimited file required by Circos for plotting.

- Note: we manually edit the highlight files in a text editor to change
  the coloring of sterile tissues to a lighter shade (i.e., ‘blue’
  becomes ‘vlblue’ \[very light blue\]).

### Example terminal code:

`python3 2_Circos_highlight.py input.txt > highlight.txt`

<u>3_Circos_links.py script:</u>

- This script identifies the tissues that contain the same barcodes and
  defines the fraction of each wedge containing a shared barcode (i.e.,
  bands).

- The output of this script is a tab-delimited file that reports all
  unique linkages between pairs of tissues (non-desiminating barcodes
  are not reported)

- <u>Note:</u> this produces a record of all pairwise linkages between
  tissues sharing the same barcode, but does not specify which tissue
  should be the origin of spread (e.g., from sites of highest CFU).
  Manual editing is needed to re-orient dissemination from putative
  origin sites.

- The output of this script (i.e., ‘link.txt’) is a tab-delimited file
  required by Circos for plotting.

### Example terminal code:

`python3 3_Circos_link.py input.txt > link.txt`

<u>4_Circos_link_rules.py script:</u>

- The configuration file for the Circos software requires ‘rules’ that
  define which links are present and how they will be colored. This
  script identifies the tissues that contain the same barcodes and
  defines the fraction of each wedge containing a shared barcode (i.e.,
  bands). It then reports out this information as text that can be copy
  and pasted directly into the Circos configuration file.

- The output of this script is a text file that should be opened, copied
  and pasted into the Circos configuration file (see part C).

- <u>Note:</u> You may need to manually edit the rules text and color
  based on how links were manually edited above.

### Example terminal code:

`python3 4_Circos_rules_link.py input.txt > rules.txt`

## B. Manual generation of additional metadata files

Circos allows the inclusion of additional information around the graph
as tracks. In this work, we included two additional pieces of information:
the time of PET-CT detection for the tissues and the total Mtb CFU
burden in each tissue at time of necropsy. To plot this information, we
manually generated two additional files:

- ‘PETCT.txt’ is a tab-delimited file that follows the highlight.txt
  format. In this case, we replaced the coloring to reflect tissues
  detected by PET-CT at different times. (Note: as this file was
  generated separately the PET-CT information is not present on the
  input.txt file).

- ‘CFUs.txt’ is a tab-delimited file in which the last column represents
  the log10-transformed Mtb CFU burden for each tissue. (Note: as this
  file was generated separately, the CFU information is not present in
  the input.txt file). This file will be plotted by Circos as a
  histogram track.

## C. Editing the configuration file and Circos plotting:**

In each NHP folder, there is a ‘xxx.conf’ file that specifies all the
tracks and parameters needed to generate the Circos plots in this study.
You will need to specify the output txt files (from Parts A & B) in
several places in the configuration file. Specifically:

- You will need to point karyotype to the ‘karyotype.txt’ file generated
  by script 1

- In the \<highlights\> block, you will need to specify the
  ‘highlight.txt’ file generated by script 2. The PET-CT information
  represents a second highlight track, which you will specify as the
  ‘PETCT.txt’ file

- In the \<plot\> block, you will point to the CFUs.txt file to create a
  histogram track

- In the \<link\> block, you will point to the link.txt file to create
  ribbons connecting tissues sharing the same barcode

- To define the coloring of the links, you will copy the text in the
  rules.txt file and paste it between the \<rules\> and \</rules\>
  block.

Finally, run the Circos program specifying the updated configuration
file to be used. The output of this script will be two plots in
different file formats: ‘circos.png‘ and ‘circos.svg’.

### Example terminal code:

`circos -conf NHP3416.conf`
