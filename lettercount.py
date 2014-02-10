# AMY: Is there a way to do this without a nested for-loop using the tools we know?

from sys import argv

script, filename = argv

openfile = open(filename)
readfile = openfile.read().lower()

for i in range(97,123):
   counter = 0
   for letter in readfile:
      if ord(letter) == i:
         counter +=1
   print counter

openfile.close()

