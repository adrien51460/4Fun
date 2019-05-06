"""
Brute-Forcing a classic probability excercice (from HackerRank)

Problem: Pick up from each urn a ball (3 urns (X,Y,Z) with a certain number of red and black balls).
         What is the probability of getting 2 red balls and a black one ?
"""

import itertools
from fractions import Fraction

b, r = [1], [0]
X = b*3 + r*4
Y = b*4 + r*5
Z = b*4 + r*4
r = [(i)for i in itertools.product(X,Y,Z)] 
e = list(map(lambda x : sum(x) == 1,r))
a=Fraction(e.count(True),len(e))
print(a)
