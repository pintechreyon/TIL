import sys
from itertools import combinations
N, M = map(int, sys.stdin.readline().split())
A = list(combinations(list(range(N)), M))
print(len(A))