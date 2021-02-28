# for generating random numbers
#!/usr/bin/env python3

from random import seed
from random import shuffle

seed(1)

seq = [i for i in range(100)]
#shuffle(seq)
print(seq)
