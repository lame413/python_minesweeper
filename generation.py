#!/usr/bin/env python

import random
import os

def generate_map(w, h, m):
	field = [[0] * w for i in range(h)]

	x = 0
	while x < m:
		r1 = random.randrange(h)
		r2 = random.randrange(w)
		if field[r1][r2] != 'B':
			field[r1][r2] = 'B'
			x += 1

	for i in range(h):
		for j in range(w):
		    if field[i][j] == 'B':
		      continue
		    else:
		        if i != h-1 and field[i+1][j] == 'B':
		          field[i][j] = field[i][j]+1
		        if i != h-1 and j != w-1 and field[i+1][j+1] == 'B':
		          field[i][j] = field[i][j]+1
		        if j != w-1 and field[i][j+1] == 'B':
		          field[i][j] = field[i][j]+1
		        if i != 0 and j != w-1 and field[i-1][j+1] == 'B':
		          field[i][j] = field[i][j]+1
		        if i != 0 and field[i-1][j] == 'B':
		          field[i][j] = field[i][j]+1
		        if i != 0 and j != 0 and field[i-1][j-1] == 'B':
		          field[i][j] = field[i][j]+1
		        if j != 0 and field[i][j-1] == 'B':
		          field[i][j] = field[i][j]+1
		        if i != h-1 and j != 0 and field[i+1][j-1] == 'B':
		          field[i][j] = field[i][j]+1

	return field

def draw_map(field):
	for i in range(len(field)):
		print(' '.join(str(x) for x in field[i]))
	return

map = generate_map(30,10,30)

posX = 0
posY = 0

while true
	mapTmp = map
	os.system("clear")
	draw_map(map)
