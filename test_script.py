#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
a script to run pythons file in some subdirectory
'''

import os
import glob


# get current directory without hidden folder
folders = glob.glob('*/')
print folders

# move into each folder
for f in folders:
    print f
    os.chdir(f)
    py_files = glob.glob('*.py')
    # run py files in the folder
    for i in py_files:
        print 'run ', i
        print '==============================='
        os.system('python ' + i)
    # return to parent folder
    os.chdir('..')

