# -*- coding: utf-8 -*-
"""
Created on Sun Jul 31 19:14:59 2016
@author: javier
"""


#read this https://github.com/pbugnion/gmaps

import json
import glob
import os
from servelParser import *
import xlrd
import sys
import csv
import json

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

    
#-------------------------------------------------------------------------------

pdfServelPath = './padron/' #the path where you have all the pdf
files = [name for name in glob.glob(os.path.join(pdfServelPath, '*.pdf'))] #search each pdf file


for i in range(len(files)):
    archivo = files[i]
    #Parse files
    servelParser(archivo)
