#!/usr/bin/env python
import os
import glob
import subprocess
print '######################
print 'Welcome to AutoSPAdes'
print '######################
print ''
print ''
directory = raw_input("Path to directory containing gzipped FastQ reads: ")
outputpath = raw_input("Path to output Fasta assemblies in: ")
print 'Assemblies will be collectively copied into your output path with logical filenames'
print 'Do you want to remove assembly subdirectories after use?'
choice = raw_input("Y/N: ").lower()
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
gzip = list(glob.glob(os.path.join(directory, '*.gz')))
for gz, in zip(gzip):
    subprocess.check_call(['gunzip', gz])
    subprocess.call(['rm', '*.gz'])
r1files = list(glob.glob(os.path.join(directory,'*R1*.fastq')))
r1files.sort()
r2files = list(glob.glob(os.path.join(directory, '*R2*.fastq')))
r2files.sort()
rawname = [x.split(directory)[1].split('_')[0] for x in r1files]
rawname.sort()
subdirectories = [directory + x for x in rawname]
for opt1, opt2, opt3, in zip(r1files, r2files,subdirectories):
    subprocess.call(['spades.py', '--pe1-1', opt1, '--pe1-2', opt2, '-o', opt3])
fastadirectories = [directory + x + '/scaffolds.fasta' for x in rawname]
fastanames = [x + '.fasta' for x in rawname]
fastaoutput = [outputpath + x for x in fastanames]
fastaremove = [directory + x + '/' for x in rawname]
print fastadirectories
print fastanames
print fastaoutput
print fastaremove
for var1, var2, in zip(fastadirectories, fastaoutput):
    subprocess.call(['cp', var1, var2])
yes = set(['yes','y','ye'])
no = set(['no','n',''])
if choice in yes:
    for remove, in zip(fastaremove):
        subprocess.check_call(['rm','-r', remove])
    print ''
    print ''
    print ''
    print '#'
    print '##'
    print '###'
    print '####'
    print '#####'
    print '######'
    print '#######'
    print '########'
    print '#########'
    print '##########'
    print '###########'
    print '############'
    print '#############'
    print '##############'
    print '###############'
    print 'Job Completed!'
    print '###############'
    print ''
    print ''
    print 'Subdirectories and .gz files scrubbed.'
    print ''
    print ''
    print 'Fasta files located in:',
    print outputpath
    print ''
    print ''
    print 'FastQ files unzippd and stored in: ',
    print directory
    print ''
    print ''
    print 'Author: www.stevendunn.co.uk'
    print ''
    print ''
    print 'Goodbye!'
    print '##############'
if choice in no:
    print ''
    print ''
    print ''
    print '#'
    print '##'
    print '###'
    print '####'
    print '#####'
    print '######'
    print '#######'
    print '########'
    print '#########'
    print '##########'
    print '###########'
    print '############'
    print '#############'
    print '##############'
    print '###############'
    print 'Job Completed!'
    print '###############'
    print ''
    print ''
    print '.gz files scrubbed'
    print ''
    print ''
    print 'Fasta subdirectories and FastQ reads located in: ',
    print directory
    print ''
    print ''
    print 'Fasta files collected and stored in: ',
    print outputpath
    print ''
    print ''
    print 'Author: www.stevendunn.co.uk'
    print ''
    print ''
    print 'Goodbye!'
    print '##############'
