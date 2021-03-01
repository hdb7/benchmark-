#!/usr/bin/env python3 

from datetime import datetime
import os 
import sys
from colorama import Fore,Back,Style

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
    
    # calculate the running time of algo in milliseconds
    rt = float((t2_in_sec - t1_in_sec) * 1000) 
    return rt

result = benchmark()

reset_color = "\u001b[0m"
colored_text1 = Fore.YELLOW + "[" + Back.CYAN + Fore.BLACK + " Time taken " + reset_color + Fore.YELLOW+"]" + Fore.CYAN + " --> " + reset_color
colored_text2 = Fore.GREEN + str(result) + " milliseconds\n" + reset_color
colored_result = colored_text1 + colored_text2
os.system("clear")
print(colored_result)

#Notes : If u want to apply 'calculate_average_value()' then just
#uncomment it & comment the above code by removing '#'
"""
algorithm_results = []
def calculate_average_value():
    #change the range if u want 
    for i in range(20):
        algorithm_results.append(benchmark())
    return (sum(algorithm_results)/len(algorithm_results))

result = calculate_average_value()

reset_color = "\u001b[0m"
colored_text1 = Fore.YELLOW + "[" + Back.CYAN + Fore.BLACK + " Time taken " + reset_color + Fore.YELLOW+"]" + Fore.CYAN + " --> " + reset_color
colored_text2 = Fore.GREEN + str(result) + " milliseconds\n" + reset_color
colored_result = colored_text1 + colored_text2
os.system("clear")
print(colored_result)

"""
