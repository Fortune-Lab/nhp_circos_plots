**<u>Instructions for generating Circos Plots</u>**

<u>Input barcoding file:</u>

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

<u>Python script usage general instructions:</u>

- Create folders for each NHP and using the input barcode file for each
  NHP (see above), run the following 4 scripts independently, generating
  individual output files.

- Create a Circos configuration file (e.g., ‘xxxx.conf’ for each NHP
  that points to the newly generated files (see Part C).

- Install Circos software and plot using Circos configuration file for
  each NHP. Manually update the configuration file to change coloring,
  sample ordering and formatting.

1.  **<u>Python scripts</u>**

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

**Example terminal code:**

python3 1_Circos_chrombands.py input.txt \> karyotype.txt

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

**Example terminal code:**

python3 2_Circos_highlight.py input.txt \> highlight.txt

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

**Example terminal code:**

python3 3_Circos_link.py input.txt \> link.txt

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

**Example terminal code:**

