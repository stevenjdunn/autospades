directory = raw_input("Path to directory containing FastQ reads: ")
import os
import glob
r1files = list(glob.glob(os.path.join(directory,'*R1*.fastq')))
r1files.sort()
r2files = list(glob.glob(os.path.join(directory, '*R2*.fastq')))
r2files.sort()
rawname = [x.split(directory)[1].split('_')[0] for x in r1files]
rawname.sort()
import subprocess
for r1, r2, out,in zip(r1files, r2files,rawname):
    subprocess.check_call(['spades.py', '--pe1-1', r1, '--pe1-2', r2, '-o', out])
print '#######################################################################'
print 'Want to quickly move all assemblies to a single file? Run automove.py!'
print 'Available at https://github.com/stevenjdunn/automove'
print '#######################################################################'
print ''
print 'www.stevendunn.co.uk'
print ''
print '#############'
print 'Job Finished!'
print '#############'
