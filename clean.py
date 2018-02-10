# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 00:27:07 2018

@author: nikola
"""
import codecs
def clean(filename, extension = '.csv'):
    with codecs.open(filename + extension, 'w', 'utf-8') as out:
        file = codecs.open(filename, 'r', 'latin-1')
        for filedata in file:
            filedata = filedata.replace('\xe8', 'c')
            filedata = filedata.replace('\xe6', 'c')
            filedata = filedata.replace('\xf0', 'd')
            filedata = filedata.replace('\x9a', 's')
            filedata = filedata.replace('\x9e', 'z')
            out.write(filedata)
        file.close()
