import re

#first part of task
input = open("advent31", "r")
possibles = 0
while True :
 sides = [int(val) for val in re.findall('\d+', input.readline())]
 if len(sides) == 0:
 	break
 if sides[sides.index(max(sides))] < 0.5 * sum(sides):
  possibles += 1
print(possibles)  
input.close()

#second part of task
input = open("advent31", "r")
possibles = 0
while True :
 sides = [ [int(val) for val in re.findall('\d+', input.readline())] for i in range(0,3)] 
 if len(sides[0]) == 0:
 	break
 for j in range(0, 3):
  col = [sides[i][j] for i in range(0,3)]
  if sides[col.index(max(col))][j] < 0.5 * sum(col):
   possibles += 1
print(possibles)  
input.close()
