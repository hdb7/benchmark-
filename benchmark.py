#dependencies required for performing this task
from datetime import datetime
import os 
import sys

def benchmark():
    
    #command required for running algorithm
    cmd = "python3 " + sys.argv[1]
    
    #get/return starting time of algorithm
    t1 = datetime.now()
    
    #running your algorithm
    os.system(cmd)
    
    #get/return ending time of algorithm
    t2 = datetime.now()
    
   
    
    #<algorithm for calcalulating time taken to complete execution of program/algorithm>
    t1_format = t1.strftime("%H:%M:%S")
    a = t1_format.split(":")

    t2_format = t2.strftime("%H:%M:%S")
    b = t2_format.split(":")

    t1_in_sec = int(a[0]) * 3600 + int(a[1]) * 60 + int(a[2]) 
    t2_in_sec = int(b[0]) * 3600 + int(b[1]) * 60 + int(b[2]) 
 
    dt = t2_in_sec - t1_in_sec 
    #</algorithm for calcalulating time taken to complete execution of program/algorithm>

    #return or give execution time in second(sec)
    return dt

#display the result in console or screen
print("[ Time taken --> ",benchmark(),"second ]")


#note
#pass your filename containing algorithm or program as an argument in command line or terminal
#example :  $ python3 benchmark.py example_algorithm/program.py 
#Thank you, feel free to give pull request