#first part of task
input = open("advent31", "r")
possibles = 0
while True :
 sides = [0, 0, 0]
 symbol = input.read(1)
 if len(symbol) == 0:
  break
 while symbol == ' ':
  symbol = input.read(1)
 i = 0
 while symbol != '\n':
  if symbol == ' ':
   i += 1
   while symbol == ' ':
    symbol = input.read(1)
  else:
   sides[i] = sides[i]*10 + ord(symbol) - ord('0')
   symbol = input.read(1)
 max = 0
 for j  in [1,2]:
  if sides[max] < sides[j]:
   max = j 
 if sides[max] < 0.5 * sum(sides):
  possibles += 1
print(possibles)  
input.close()

#second part of task
input = open("advent31", "r")
possibles = 0
while True :
 sides = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
 ]

 symbol = input.read(1)
 if len(symbol) == 0:
  break

 for i in range(0, 3):
  j = 0
  symbol = input.read(1)
  while symbol == ' ':
   symbol = input.read(1)
  while symbol != '\n':
   if symbol == ' ':
    j += 1
    while symbol == ' ':
     symbol = input.read(1)
   else:
    sides[i][j] = sides[i][j]*10 + ord(symbol) - ord('0')
    symbol = input.read(1)
 for j in range(0, 3):
  max = 0
  for i  in [1,2]:
   if sides[max][j] < sides[i][j]:
    max = i
  if sides[max][j] < 0.5 * sum([sides[k][j] for k in range(0,3)]):
   possibles += 1
print(possibles)  
input.close()
