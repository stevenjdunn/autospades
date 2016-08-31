# autospades.py
Automatic SPAdes assemblies directly from Illumina output files.

Dependencies:
SPAdes - http://bioinf.spbau.ru/spades

The script assumes your filenames are in standard Illumina output format.

Before use, transfer your gzipped fastq.gz files from the MiSeq to a single directory on your workstation.

On execution, you will be prompted for the directory containing your files - use a full path (e.g. /users/me/Desktop/reads/).
The script will assemble all reads present in the directory, collect the 'scaffolds.fasta' output from each subdirectory and rename them according to the Sample ID.


If you have any questions, please visit my website www.stevendunn.co.uk
