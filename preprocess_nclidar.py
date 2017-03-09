#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
preprocess_nclidar.py

what? 
- accesses and unarchives (unzips) compressed archives in the folder pointed
to by fpath
- from each unzipped archive, the ASCII text file is located, open and its
contents read
- the read content are written (concatenated) to a target file (ft) 
- once the concatenation is comleted, the open files are closed and buttoned
up and any other clean up conducted

NOTE that the target file (tf) could get really big if you have a lot of 
really big files to load, read, and copy. Plan accordingly.


Created on Fri Mar  3 14:20:57 2017  Paul P

@author: paulp
"""

import os

# fi = the current input file,  ft= target file
fpath ='/Volumes/Beaker/projects/coastal_plains/LiDAR/'
targetFile='HalifaxNC.csv'

# get a list of all the zipped archive files in the fpath subdir:
zf = [f for f in os.listdir(fpath) if os.path.isfile(os.path.join(fpath, f))]

# then, unzip everything in the zf list and drop these into fpath:
for fx in zf:
    print(fx)
    os.system('unzip '+fpath+fx+' -d '+fpath)
    
# get list of all the .txt files that were just unarchived (unzipped):
txf=[f for f in os.listdir(fpath) if(f.endswith('.txt'))]

# traverse each file in txf and concatenate contents into target file ft:
ft=open(fpath+targetFile, 'a' )

for tx in txf:
    print('Processing file:', tx, 'Are we done yet?  Nope.')
    tmpf = open(fpath+tx, 'r')
    lines = tmpf.readlines()     # read the entire .txt file
    for index, line in enumerate(lines):          
        if(index != 0):            # skip the first line (hdr) in each file
            l = line.split(',')
            x=float(l[0]); y=float(l[1]); z=float(l[2])
            X=x*0.304800609601         # conv survey feet to meters
            Y=y*0.304800609601
            Z=z
    
            ft.write(str('%.3f' % X)+','+str('%.3f' % Y)+','+str(Z)+'\n')
            
    tmpf.close()
    
ft.close()

print('Now we\'re done.')
