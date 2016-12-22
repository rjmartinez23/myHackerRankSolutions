#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

alice_points = [a0, a1, a2]
bob_points = [b0, b1, b2]

alice = 0
bob = 0 
for i in range(0, len(alice_points)):
  if alice_points[i] > bob_points[i]:
    alice +=1
  elif bob_points[i] > alice_points[i]:
    bob += 1

print('{} {}'.format(alice, bob))
