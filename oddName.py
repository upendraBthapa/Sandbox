__author__ = 'jc449735'
"""
 upendra b thapa
"""
valid = False
name=input("enter your name")
L=len(name)
while not valid:
  if name != "" and not name.isspace():
    valid = True

for l in range(0,L,2):
    print(name[l])