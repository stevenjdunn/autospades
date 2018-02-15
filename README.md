# autospades.py
Automatic SPAdes assemblies directly from Illumina output files.

Dependencies:
SPAdes - http://bioinf.spbau.ru/spades

# Quick Start
autospades.py -i <path to input directory containing fastq.gz's> -o <Path to output finished assemblies>

# Options
usage: autospades.py -i < path to input directory > -o < path to ouput directory > [-h] [-c] [-rm] [-bug]

optional arguments:

       -h, --help            show this help message and exit
       -i <INPUT>, --input <INPUT>
                            Path to directory containing raw Illumina reads.
      -o <OUTPUT>, --output OUTPUT
                            Path to output destination.
      -c, --careful         Invoke SPAdes using the --careful flag
      -rm, --remove         Removes assembly subdirectories after use.
      -bug, --debug         Print all generated lists to stdout + log for
                            troubleshooting, and exit.
  
# Information
The script assumes your filenames are in standard Illumina output format.

Before use, transfer your gzipped fastq.gz files from the MiSeq to a single directory on your workstation and pass that directory to autospades using the -i flag. 

The script will assemble all reads present in the directory, collect the 'scaffolds.fasta' output from each subdirectory and rename them according to the Sample ID.

# Questions
# It isn't working. Why?
Probably due to the filenames. The script is written with the default Illumina naming system in mind, that is to say the raw output directly from the sequencer. If you've renamed your files, or if Illumina update their naming scheme, things will break. To diagnose you can run the program with the -bug flag, which will print all of the lists to stdout + autospades.log. If you really can't make sense of it and are struggling, raise an issue and I'll take a look.

# How can I add a flag to spades?
Lines 182-190 contain the call that invokes Spades. If you run with careful, edit line 185. Otherwise, it'll be line 190. All you need to do is add your flag in quotation marks, followed by a comma, followed by your optional variable in quotation marks, followed by a final comma.

For example, if we wanted to specify how many threads SPAdes should use while running in careful mode, we'd change line 185 from:
       
       subprocess.call(['spades.py', '--careful', '--pe1-1', opt1, '--pe1-2', opt2, '-o', opt3])
to:
      
      subprocess.call(['spades.py', '--careful', '-t', '8', '--pe1-1', opt1, '--pe1-2', opt2, '-o', opt3])

# Why did you choose to do X with Y in Z way?
Because I am inexperienced and write code to fix my own problems before packaging in a slightly neater way. I make my scripts on the train during my commute with limited internet access, so I can only sporadically check StackOverflow answers for my limitless questions. I’m sure 90% of my code can be achieved in a neater and more pythonic way.

# Why import and use time for pointless delays?
I found on my (admittedly ancient) MacBook air that python seemed to move too fast for its own good, and I’d get errors when calling via subprocess. I started by adding a delay to mitigate this on my (and presumably some other older) machines. I also added a couple at the start of the script to give users a chance to check their directory inputs and escape if necessary.

# But I don’t want your stinking delays!?
You can parse the script to remove any line containing ‘time’ with no ill effects to the underlying pipeline. 
