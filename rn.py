#!/usr/bin/env python3
#This file is a part of benchmark for testing the benchmark.py
# for generating random numbers

from random import seed
from random import shuffle

seed(1)
seq = [i for i in range(10000)]
shuffle(seq)
print(seq)
