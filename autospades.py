#!/usr/bin/env python
import os
import glob
import subprocess
import argparse
import re
import sys
import time

# Argparse argument setup
parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input", required=True, help="Path to directory containing raw Illumina reads.")
parser.add_argument("-o", "--output", required=True, help="Path to output destination.")
parser.add_argument("-c", "--careful", action="store_true", help="Invoke SPAdes using the --careful flag")
parser.add_argument("-rm", "--remove", action="store_true", help="Removes assembly subdirectories after use." )
parser.add_argument("-bug", "--debug", action="store_true", help="Print all generated lists to stdout + log for troubleshooting, and exit.")
args = parser.parse_args()

# Colour set up
class colours:
    warning = '\033[93m'
    blue = '\033[94m'
    bold = '\033[1m'
    term = '\033[0m'

# Logger set up
ansi_rm = re.compile(r'\x1b\[[0-9;]*m')
class Logger(object):
    def __init__(self):
        self.terminal = sys.stdout
        self.log = open("autospades.log", "w")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(re.sub(ansi_rm, '', message))

sys.stdout = Logger()


# Welcome Message
print ''
print ''
print  colours.bold + '######################'
print 'Welcome to AutoSPAdes'
print '######################' + colours.term
print ''

# Check output path exists, try to write.
if not os.path.exists(args.output):
    try:
        os.makedirs(args.output)
        print 'Output directory created.'
        print ''
    except Exception:
        print colours.warning + 'Could not create output directory!'
        print ''
        print 'Check that the path is correct and that you have the required permissions.'
        print ''
        print ''
        print colours.bold + '#############'
        print 'Script Failed'
        print '#############' + colours.term
        print ''
        print 'Errors written to:' + os.getcwd() + '/' + 'autospades.log'
        print ''
        sys.exit(1)

# Directory orientation
invoked_from = os.getcwd()
os.chdir(args.input)
directory = os.getcwd()
os.chdir(invoked_from)
os.chdir(args.output)
outputpath = os.getcwd()
os.chdir(invoked_from)

# Log directories
print colours.blue + "Path to raw Illumina reads:" + colours.term,
print directory
print ''
print colours.blue + "Path to output directory:" + colours.term,
print outputpath
time.sleep(1)
print ''
print 'Commencing assembly...'
time.sleep(1)

# List comprehension
r1files = list(glob.glob(os.path.join(directory,'*_R1_*')))
r1files.sort()
r2files = list(glob.glob(os.path.join(directory, '*_R2_*')))
r2files.sort()
rawname = [x.split(directory)[1].split('_')[0] for x in r1files]
rawname.sort()
subdirectoriesraw = [directory + x + '_' for x in rawname]
subdirectoriesraw.sort()
subdirectories = [x.split('_')[0] + '/' for x in subdirectoriesraw]
fastadirectories = [x + 'scaffolds.fasta' for x in subdirectories]
fastanames = [x + '.fasta' for x in rawname]
fastaoutput = [outputpath + x for x in fastanames]

# Debug output
if args.debug:
    print ''
    print '###########'
    print 'Debug Lists'
    print '###########'
    print ''
    print 'r1files: ',
    print r1files
    print 'r2files: ',
    print r2files
    print 'rawname: '
    print rawname
    print 'subdiretoriesraw: '
    print subdirectoriesraw
    print 'subdirectories: '
    print subdirectories
    print 'fastadirectories: '
    print fastadirectories
    print 'fastanames: '
    print fastanames
    print 'fastaoutput: '
    print fastaoutput
    print ''
    print '###########'
    sys.exit(1)

# Check generated read lists contain >0 files, and are equal in length
length = len(r1files)
if len(r2files) != length:
    print ''
    print ''
    print colours.warning + colours.bold + "#######"
    print 'WARNING!'
    print '########' + colours.term
    print colours.warning + ''
    print 'Detected odd number of reads.'
    print ''
    print 'Input directory should contain paired end read data, with filenames ending in _R1.fastq and _R2.fastq'
    print ''
    print 'The supplied input directory: ',
    print colours.term + directory
    print colours.warning + ''
    print 'Was found to contain the following R1 files:' + colours.term
    print r1files
    print colours.warning + ''
    print 'and the following R2 files:' + colours.term
    print r2files
    print ''
    print ''
    print colours.warning + 'Please check these lists and the input directory to ensure all files are present and accounted for.'
    print ''
    print colours.bold + '#############'
    print 'Script Failed'
    print '#############' + colours.term
    print ''
    print 'Errors written to:' + invoked_from + '/' + 'autospades.log'
    print ''
    sys.exit(1)
    
if len(r1files) == 0:
    print ''
    print ''
    print colours.warning + colours.bold + "########"
    print 'WARNING!'
    print '########' + colours.term
    print colours.warning + ''
    print 'Could not detect any read files.'
    print ''
    print ''
    print colours.warning + 'Please check the input directory to ensure all files are present and accounted for.'
    print ''
    print colours.bold + '#############'
    print 'Script Failed'
    print '#############' + colours.term
    print ''
    print 'Errors written to:' + invoked_from + '/' + 'autospades.log'
    print ''
    sys.exit(1)

# Spades invocation --careful
if args.careful:
    for opt1, opt2, opt3, in zip(r1files, r2files, subdirectories):
        subprocess.call(['spades.py', '--careful', '--pe1-1', opt1, '--pe1-2', opt2, '-o', opt3])

# Default spades invocation
if not args.careful:
    for opt1, opt2, opt3, in zip(r1files, r2files, subdirectories):
        subprocess.call(['spades.py', '--pe1-1', opt1, '--pe1-2', opt2, '-o', opt3])

# FASTA organisation (rename and collect)
time.sleep(1)
print ''
print colours.bold + '###################'
print 'SPAdes has finished'
print '###################' + colours.term
print ''
time.sleep(1)
for var1, var2, in zip(fastadirectories, fastaoutput):
    try:
        subprocess.check_call(['cp', var1, var2])
    except Exception:
        print colours.warning + ''
        print 'Could not locate assemblies. Please check spades output logs for errors.'
        time.sleep(1)
        print '' + colours.term
        sys.exit(1)


# Try directory removal if requested
if args.remove:
    try:
        for remove, in zip(subdirectories):
            subprocess.check_call(['rm','-r', remove])
        print ''
        print ''
        print ''
        print colours.bold + '###############'
        print 'Job Completed!'
        print '###############' + colours.term
        print ''
        print ''
        print 'Subdirectories scrubbed.'
        print ''
        print ''
        print colours.blue + 'Fasta files located in:' + colours.term,
        print outputpath
        print ''
        print ''
        print colours.blue + 'FastQ files unzippd and stored in: ' + colours.term,
        print directory
        print ''
        print ''
        print 'Author: www.github.com/stevenjdunn'
        print ''
        print ''
        print 'Goodbye!'
        print '##############'
    except Exception:
        print ''
        print colours.warning + colours.bold + "#######"
        print 'WARNING!'
        print '########' + colours.term
        print ''
        print ''
        print colour.warning + 'Could not remove assembly subdirectories as requested.' + colours.terminal
        print ''
        print ''
        print colours.blue + 'Fasta files located in:' + colours.term,
        print outputpath
        print ''
        print ''
        print colours.blue + 'FastQ files unzippd and stored in: ' + colours.term,
        print directory
        print ''
        print ''
        print 'Author: www.github.com/stevenjdunn'
        print ''
        print ''
        print 'Goodbye!'
        print '##############'

# No removal script end
if not args.remove:
    print ''
    print ''
    print colours.bold + '###############'
    print 'Job Completed!'
    print '###############' + colours.term
    print ''
    print ''
    print colours.blue + 'Fasta subdirectories and FastQ reads located in: ' + colours.term,
    print directory
    print ''
    print ''
    print colours.blue + 'Fasta files collected and stored in: ' + colours.term,
    print outputpath
    print ''
    print ''
    print 'Author: www.github.com/stevenjdunn'
    print ''
    print ''
    print 'Goodbye!'
    print '##############'
