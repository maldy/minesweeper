#!/usr/bin/env python

import random

class Minesweeper:

	def __init__(self, size=10, n_mines=10):
		self.size=size 
		self.n_mines=n_mines
		self.mines = []
		self.explored = []
		self.game_map = [[0 for col in range(size)] for row in range(size)]

		for i in range(n_mines):
			self.mines.append(None)
			while True:
				self.mines[i] = (random.randint(0,size-1),random.randint(0,size-1))
				if self.mines[i] not in self.mines[0:i]:
					break

		for mine in self.mines:
			self.game_map[mine[0]][mine[1]] = -1
			squares = self.safe_squares(mine[0], mine[1])
			for square in squares:
				self.game_map[square[0]][square[1]] += 1

	def safe_squares(self, x, y):
		squares = []
		for i in [x-1,x,x+1]:
			for j in [y-1,y,y+1]:
				if i==x and j==y: continue
				if i >=0 and i < self.size and j >=0 and j < self.size and self.game_map[i][j] != -1:
					squares.append((i,j))
		return squares

	def proceed(self, x, y):
		if (x,y) in self.mines:
			print "KABOOM you're dead."
			self.explored.append((x,y))
			self.print_map()
			return False
		self.floodfill(x,y)
		self.print_map()
		if len(self.explored)== self.size**2 - self.n_mines:
			print "BOOYAH you win."
			return False
		return True
		

	def floodfill(self,x,y):
		self.explored.append((x,y))
		if self.game_map[x][y] == 0:
			squares = self.safe_squares(x,y)
			for square in squares:
				if square not in self.explored: self.floodfill(square[0],square[1])

	def print_map(self):
		print "======================="
		print "  ",
		for i in range (1,self.size+1):
			print i,
		print
		for i in range(0,self.size):
			print "%d:"%(i+1),
			for j in range(0, self.size):
				if (i,j) in self.explored:
					if self.game_map[i][j]==0:
						print " ",
					elif self.game_map[i][j]==-1:
						print "X",
					else:
						print self.game_map[i][j],
				else:
					print "-",
			print "|"
		print "======================="
game = Minesweeper(9,10)
(x, y) = (random.randint(1,9),random.randint(1,9))
while game.proceed(x-1,y-1):
	x = int(raw_input("x: "))
	y = int(raw_input("y: "))
