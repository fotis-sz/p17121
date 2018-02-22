import string
import random
import sys
import os
name = raw_input("give filename")

fo=open(name,"r")
data=fo.read()
fo.close()

result = sorted(set(
    word.strip(string.punctuation)
    for line in open(name)
    for word in line.split()))

plithos = result.__len__()

pinakas = [];

count = 0


for x in range(0,plithos ):
   string = result[x]
   flag = string.islower()
   if flag is True:
      pinakas.insert(x,string)
      count += 1



print "Aytes einai oi lekseis me peza " , pinakas

if count%3 == 0 :
   grammes = count/3
else: grammes = count/3 +1

triades = [[0 for x in range(3)] for y in range(grammes)]



for x in range(0,grammes):
   for y in range(0,3):
      triades[x][y] = pinakas[x+y]


print "Autes einai oi triades" , triades
