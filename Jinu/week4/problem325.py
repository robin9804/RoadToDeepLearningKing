
import math

max = 108

for i in range(max):
    for j in range(max):

        if ( i <= j ) & ( math.sqrt(i) + math.sqrt(j) == math.sqrt(108)) :

            print('(', i, j, ')')