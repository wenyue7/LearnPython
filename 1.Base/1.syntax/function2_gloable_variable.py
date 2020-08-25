#!/usr/bin/python
# Filename: func_local.py
x=50
def func():
  global x
  print ('x is', x)
  x = 2
  print ('Changed local x to', x)
func()
print('variable x is:',x)
