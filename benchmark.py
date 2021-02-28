#!/usr/bin/env python3 

from datetime import datetime
import os 
import sys

def benchmark():
    argc = len(sys.argv)-1
    if argc == 1:
        cmd = sys.argv[1]
    else:
        cmd = sys.argv[1] +" "+ sys.argv[2]

    t1 = datetime.now()       #starting time
    os.system(cmd)            #execute algorithm
    t2 = datetime.now()       #ending time
    
    t1_format = t1.strftime("%H:%M:%S")
    a = t1_format.split(":")

    t2_format = t2.strftime("%H:%M:%S")
    b = t2_format.split(":")

    t1_in_sec = int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2]) 
    t2_in_sec = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2]) 
    # calculate the running time of algo in sec
    rt = float(t2_in_sec - t1_in_sec) 
    return rt

print("[ Time taken --> ",benchmark(),"second ]")
