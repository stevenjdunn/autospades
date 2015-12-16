#!/usr/bin/env python
import os
import glob
import subprocess
print ''
print ''
print '######################'
print 'Welcome to AutoSPAdes'
print '######################'
print ''
print ''
directory = raw_input("Path to directory containing gzipped FastQ reads: ")
outputpath = raw_input("Path to output Fasta assemblies in: ")
print 'Assemblies will be collectively copied into your output path with logical filenames'
print 'Do you want to remove assembly subdirectories after use?'
choice = raw_input("Y/N: ").lower()
print 'Use the careful flag?'
careful = raw_input("Y/N: ").lower()
print 'Remove .gz archives after use?'
rmgz = raw_input("Y/N: ").lower()
if not os.path.exists(outputpath):
    os.makedirs(outputpath)
gzip = list(glob.glob(os.path.join(directory, '*.gz')))
for gz, in zip(gzip):
    subprocess.check_call(['gunzip', gz])
print ''
print '#######################'
print 'Archives expanded'
print ''
print 'Beginning Assembly'
print '#######################'
r1files = list(glob.glob(os.path.join(directory,'*R1*.fastq')))
r1files.sort()
r2files = list(glob.glob(os.path.join(directory, '*R2*.fastq')))
r2files.sort()
yes = set(['yes','y','ye'])
no = set(['no','n',''])
rawname = [x.split(directory)[1].split('_')[0] for x in r1files]
rawname.sort()
subdirectoriesraw = [directory + x + '_' for x in rawname]
subdirectoriesraw.sort()
subdirectories = [x.split('_')[0] + '/' for x in subdirectoriesraw]
fastadirectories = [x + 'scaffolds.fasta' for x in subdirectories]
fastanames = [x + '.fasta' for x in rawname]
fastaoutput = [outputpath + x for x in fastanames]

if careful in yes:
    for opt1, opt2, opt3, in zip(r1files, r2files,subdirectories):
        subprocess.call(['spades.py', '--careful', '--pe1-1', opt1, '--pe1-2', opt2, '-o', opt3])
if careful in no:
    for opt1, opt2, opt3, in zip(r1files, r2files,subdirectories):
        subprocess.call(['spades.py', '--pe1-1', opt1, '--pe1-2', opt2, '-o', opt3])

for var1, var2, in zip(fastadirectories, fastaoutput):
    subprocess.call(['cp', var1, var2])
if rmgz in yes:
    for gz in zip(gzip):
        subprocess.call(['rm', gz])
    print ''
    print ''
    print '##################'
    print '.gz files scrubbed'
    print '##################'
    print ''
    print ''
if choice in yes:
    for remove, in zip(subdirectories):
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
    print 'Subdirectories scrubbed.'
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
