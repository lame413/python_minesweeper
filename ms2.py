#!/usr/bin/env python3

from string import ascii_uppercase
import random

import tkinter

def check_win(f, pf):
	for i in range(len(f)):
		for j in range(len(f[i])):
			if f[i][j] == 'B' or f[i][j] == pf[i][j]:
				continue
			else:
				return
	print('victory!')
	quit()

def check_field_on_click(w, h, f, pf):
	if pf[h][w] == ' ':
		pf[h][w] = f[h][w]
		if f[h][w] != 'B':
			if f[h][w] == 0:
				if h != len(f)-1:
					check_field_on_click(w,h+1,f,pf)
				if h != len(f)-1 and w != len(f[h])-1:
					check_field_on_click(w+1,h+1,f,pf)
				if w != len(f[h])-1 :
					check_field_on_click(w+1,h,f,pf)
				if h != 0 and w != len(f[h])-1:
					check_field_on_click(w+1,h-1,f,pf)
				if h != 0:
					check_field_on_click(w,h-1,f,pf)
				if h != 0 and w != 0:
					check_field_on_click(w-1,h-1,f,pf)
				if w != 0:
					check_field_on_click(w-1,h,f,pf)
				if h != len(f)-1 and w != 0:
					check_field_on_click(w-1,h+1,f,pf)
		else:
			print('that was a bomb')
	else:
		return


_w = 27
_h = 27
_m = 700
while _w > 26:
	_w = int(input('Please input the board width (max 26): '))
while _h > 26: 
	_h = int(input('Please input the board height (max 26): '))
while _m >= int(_w*_h/2):
	_m = int(input('Please input the number of mines (max '+str(int((_w*_h/2))-1)+'): '))


if _w * _h < _m:
	print('More mines than fields!')
	quit()

field = [[0] * _w for i in range(_h)]
player_field = [[' '] * _w for i in range(_h)]

# populate physical field with mines
x = 0
while x < _m:
  r1 = random.randrange(_h)
  r2 = random.randrange(_w)
  if field[r1][r2] != 'B':
    field[r1][r2] = 'B'
    #print('set bomb at r1='+str(r1)+', r2='+str(r2)+', x='+str(x))
    x += 1

# populate physical field with numbers dependent on mines
for i in range(_h):
  #print('loop i nr. ' + str(i))
  for j in range(_w):
    #print('loop j nr. ' + str(j))
    if field[i][j] != 'B':
      if i != _h-1 and field[i+1][j] == 'B':
          field[i][j] += 1  
      if i != _h-1 and j != _w-1 and field[i+1][j+1] == 'B':
          field[i][j] += 1
      if j != _w-1 and field[i][j+1] == 'B':
          field[i][j] += 1
      if i != 0 and j != _w-1 and field[i-1][j+1] == 'B':
          field[i][j] += 1  
      if i != 0 and field[i-1][j] == 'B':
          field[i][j] += 1
      if i != 0 and j != 0 and field[i-1][j-1] == 'B':
          field[i][j] += 1
      if j != 0 and field[i][j-1] == 'B':
          field[i][j] += 1  
      if i != _h-1 and j != 0 and field[i+1][j-1] == 'B':
          field[i][j] += 1

# main game loop
while True:
	print()
	print('    |', end = '')
	for i in range(_w):
		print(ascii_uppercase[i], end='|')
	print()
	print()

	for i in range(_h):
		print(str(i+1) + ')' + (3-len(str(i+1)))*' ' + '|', end='')
		for j in range(_w):
			print(str(player_field[i][j]), end='|')
		print('')
	
	check_win(field, player_field)

	i_w = -1
	i_h = -1

	while i_w == -1:
		i_w = input('select w: ')

		if ascii_uppercase.find(i_w.upper()) == -1:
			print('please input a character ranging from A to '+ascii_uppercase[_w-1]+'.')
			i_w = -1
			continue
		
		i_w = ascii_uppercase.index(i_w.upper())

		if int(i_w)+1 > _w:
			print('please input a character ranging from A to '+ascii_uppercase[_w-1]+'.')
			i_w = -1
			continue

	while i_h == -1:
		i_h = input('select h: ')
		if int(i_h) > _h:
			print('please input a number smaller than ' + _h)
			i_h = -1
			continue
	
	check_field_on_click(int(i_w),int(i_h)-1,field,player_field)

