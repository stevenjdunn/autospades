# autospades.py
A simple script to automate SPAdes assemblies

This script assumes you have raw paired end reads in the FastQ format, contained in a single directory.

Simply run the script and you will be prompted for the directory containing your reads - use a full path (e.g. /users/me/Desktop/reads/)

The script has some limitations...

Your isolate ID can't contain any underscores, as it uses the first underscore character to distinguish the ID from the rest of the filename. 
 
It will try to assemble all FastQ files in a directory - separate the reads you want to process into a new directory devoid of any special characters.
 
It will fail if there is not a forward and reverse read present.
 
It will fail if your reads have been renamed and no longer contain the strings 'R1' or 'R2'
 
To use the script, it's best to add it to your .bashrc - this is a text file that points your terminal to scripts and programs. First, open a terminal (Ctrl+Alt+T) and type:
 
gedit ~/.bashrc
 
 A new window will open - scroll to the bottom, add the following line, and save:
 
alias autospades.py='/home/user/scripts/autospades.py'

The output of this script can be quickly processed to include all assemblies in a single directory with logical filenames - simply run automove.py, available at: https://github.com/stevenjdunn/automove


If you have any questions, please visit my website www.stevendunn.co.uk
