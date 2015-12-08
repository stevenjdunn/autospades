# autospades.py
A simple script to automate SPAdes assemblies directly from MiSeq output files.

Before use, transfer your gzipped fastq.gz files from the MiSeq to a single directory on your workstation.

On execution, you will be prompted for the directory containing your files - use a full path (e.g. /users/me/Desktop/reads/). The script will unpack your reads, assemble each sample's genome, and if specified collect all of the resulting assemblies into a single folder. 

The script has some limitations...

Your isolate ID can't contain any underscores, as it uses the first underscore character to distinguish the ID from the rest of the filename. 
 
It will try to assemble all FastQ files in a directory - separate the reads you want to process into a new directory devoid of any special characters.
 
It will fail if there is not a forward and reverse read present.
 
It will fail if your reads have been renamed and no longer contain the strings 'R1' or 'R2'
 
To use the script, it's best to add it to your .bashrc - this is a text file that points your terminal to scripts and programs. First, open a terminal (Ctrl+Alt+T) and type:
 
gedit ~/.bashrc
 
 A new window will open - scroll to the bottom, add the following line, and save:
 
alias autospades.py='/home/user/scripts/autospades.py'


If you have any questions, please visit my website www.stevendunn.co.uk
