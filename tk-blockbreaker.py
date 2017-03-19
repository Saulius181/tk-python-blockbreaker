#!/usr/bin/env python

from tkinter import *
import random
import time

class game_controller(object):
	def new_game(self):
		self.canvas.data["Dir"] = {'x': 0.2, 'y':0.5}
		self.canvas.data["Speed"] = 5
		self.canvas.data["xTurn"] = False
		self.canvas.data["yTurn"] = False
		self.canvas.coords(self.ball, 300, 150, 320, 170)
		self.canvas.data["play"] = True
		self.root.after(20, self.moveit)	
		
	def quit(self):
		self.root.destroy()	
		
	def mouseMoved(self, event):
		if event.x <= 60:
			self.canvas.coords(self.rect, 10, 270, 110, 290)
		elif event.x >= 440:
			self.canvas.coords(self.rect, 390, 270, 490, 290)
		else:
			self.canvas.coords(self.rect, event.x-50, 270, event.x+50, 290)
	
	def moveit(self):

		if self.canvas.coords(self.ball)[3] > 300 and self.canvas.data["Dir"]['y'] > 0:
			self.canvas.coords(self.ball, -200, -120, -220, -140)
			self.canvas.data["play"] = False
		
		self.canvas.data["coordRange"] = []
		for i in range(1, self.canvas.data["Speed"]+1):
			self.canvas.data["coordRange"].append([self.canvas.coords(self.ball)[0] + (self.canvas.data["Dir"]['x'] * i), self.canvas.coords(self.ball)[1] + (self.canvas.data["Dir"]['y'] * i), self.canvas.coords(self.ball)[2] + (self.canvas.data["Dir"]['x'] * i), self.canvas.coords(self.ball)[3] + (self.canvas.data["Dir"]['y'] * i)   ])
		
		for i in self.canvas.data["coordRange"]:

			left = int(i[0]//40)*40
			top = int(i[1]//20)*20
			right = int(i[2]//40)*40
			bottom = int(i[3]//20)*20
			
			blockList = []
			
			if self.canvas.data["Dir"]['y'] > 0 and self.canvas.data["Dir"]['x'] > 0:
				if right in self.canvas.data["blockDict"] and bottom in self.canvas.data["blockDict"][right]:
					blockList.append([self.canvas.data["blockDict"][right][bottom], right, bottom])
				if left in self.canvas.data["blockDict"] and bottom in self.canvas.data["blockDict"][left]:
					blockList.append([self.canvas.data["blockDict"][left][bottom], left, bottom ])
				if right in self.canvas.data["blockDict"] and top in self.canvas.data["blockDict"][right]:
					blockList.append([self.canvas.data["blockDict"][right][top], right, top])
			elif self.canvas.data["Dir"]['y'] > 0 and self.canvas.data["Dir"]['x'] < 0:
				if left in self.canvas.data["blockDict"] and bottom in self.canvas.data["blockDict"][left]:
					blockList.append( [self.canvas.data["blockDict"][left][bottom], left, bottom] )
				if right in self.canvas.data["blockDict"] and bottom in self.canvas.data["blockDict"][right]:
					blockList.append( [self.canvas.data["blockDict"][right][bottom], right, bottom] )
				if left in self.canvas.data["blockDict"] and top in self.canvas.data["blockDict"][left]:
					blockList.append([self.canvas.data["blockDict"][left][top], left, top])
					
			elif self.canvas.data["Dir"]['y'] < 0 and self.canvas.data["Dir"]['x'] > 0:
				if right in self.canvas.data["blockDict"] and top in self.canvas.data["blockDict"][right]:
					blockList.append([self.canvas.data["blockDict"][right][top], right, top])
				if right in self.canvas.data["blockDict"] and bottom in self.canvas.data["blockDict"][right]:
					blockList.append([self.canvas.data["blockDict"][right][bottom], right, bottom])
				if left in self.canvas.data["blockDict"] and top in self.canvas.data["blockDict"][left]:
					blockList.append([self.canvas.data["blockDict"][left][top], left, top])					
			elif self.canvas.data["Dir"]['y'] < 0 and self.canvas.data["Dir"]['x'] < 0:
				if left in self.canvas.data["blockDict"] and top in self.canvas.data["blockDict"][left]:
					blockList.append([self.canvas.data["blockDict"][left][top], left, top])	
				if left in self.canvas.data["blockDict"] and bottom in self.canvas.data["blockDict"][left]:
					blockList.append([self.canvas.data["blockDict"][left][bottom], left, bottom])
				if right in self.canvas.data["blockDict"] and top in self.canvas.data["blockDict"][right]:
					blockList.append([self.canvas.data["blockDict"][right][top], right, top])
			
			for j in blockList:				
				if self.canvas.data["Dir"]['y'] > 0 and self.canvas.data["Dir"]['x'] > 0 and self.canvas.coords(j[0][0])[2] + 15 >= i[2] and self.canvas.coords(j[0][0])[3] + 15 >= i[3]:
					if self.canvas.coords(j[0][0])[0] <= i[2] and self.canvas.coords(j[0][0])[1] <= i[3]:
						if i[3] - self.canvas.coords(j[0][0])[1] > i[2] - self.canvas.coords(j[0][0])[0]:
							self.canvas.data["Dir"]['x'] *= -1
							self.canvas.data["xTurn"] = True
							self.canvas.delete(j[0][0])
							del self.canvas.data["blockDict"][j[1]][j[2]]
						else:
							self.canvas.data["Dir"]['y'] *= -1
							self.canvas.data["yTurn"] = True
							self.canvas.delete(j[0][0])
							del self.canvas.data["blockDict"][j[1]][j[2]]			
					
				elif self.canvas.data["Dir"]['y'] > 0 and self.canvas.data["Dir"]['x'] < 0 and self.canvas.coords(j[0][0])[0] -15 <= i[0] and self.canvas.coords(j[0][0])[3] +15 >= i[3]:
					if self.canvas.coords(j[0][0])[2] >= i[0] and self.canvas.coords(j[0][0])[1] <= i[3]:
						if i[3] - self.canvas.coords(j[0][0])[1] > self.canvas.coords(j[0][0])[2] - i[0]:
							self.canvas.data["Dir"]['x'] *= -1
							self.canvas.data["xTurn"] = True
							self.canvas.delete(j[0][0])
							del self.canvas.data["blockDict"][j[1]][j[2]]
						else:
							self.canvas.data["Dir"]['y'] *= -1
							self.canvas.data["yTurn"] = True
							self.canvas.delete(j[0][0])
							del self.canvas.data["blockDict"][j[1]][j[2]]		
					
				elif self.canvas.data["Dir"]['y'] < 0 and self.canvas.data["Dir"]['x'] > 0 and self.canvas.coords(j[0][0])[2] +15 >= i[2] and self.canvas.coords(j[0][0])[1] -15 <= i[1]:
					if self.canvas.coords(j[0][0])[0] <= i[2] and self.canvas.coords(j[0][0])[3] >= i[1]:
						if self.canvas.coords(j[0][0])[3] - i[1] > i[2] - self.canvas.coords(j[0][0])[0]:
							self.canvas.data["Dir"]['x'] *= -1
							self.canvas.data["xTurn"] = True
							self.canvas.delete(j[0][0])
							del self.canvas.data["blockDict"][j[1]][j[2]]
						else:
							self.canvas.data["Dir"]['y'] *= -1
							self.canvas.data["yTurn"] = True
							self.canvas.delete(j[0][0])
							del self.canvas.data["blockDict"][j[1]][j[2]]
							
				elif self.canvas.data["Dir"]['y'] < 0 and self.canvas.data["Dir"]['x'] < 0 and self.canvas.coords(j[0][0])[0] -15<= i[0] and self.canvas.coords(j[0][0])[1] -15<= i[1]:
					if self.canvas.coords(j[0][0])[2] >= i[0] and self.canvas.coords(j[0][0])[3] >= i[1]:
						if self.canvas.coords(j[0][0])[3] - i[1] > self.canvas.coords(j[0][0])[2] - i[0]:
							self.canvas.data["Dir"]['x'] *= -1
							self.canvas.data["xTurn"] = True
							self.canvas.delete(j[0][0])
							del self.canvas.data["blockDict"][j[1]][j[2]]
						else:
							self.canvas.data["Dir"]['y'] *= -1
							self.canvas.data["yTurn"] = True
							self.canvas.delete(j[0][0])
							del self.canvas.data["blockDict"][j[1]][j[2]]
				
				if self.canvas.data["yTurn"] or self.canvas.data["xTurn"]:
					break
					
			if self.canvas.data["yTurn"] or self.canvas.data["xTurn"]:
				break
					
			
			if i[3] < 290 and i[3] > 270 and self.canvas.data["Dir"]['y'] > 0:
				if self.canvas.coords(self.rect)[0] < i[2] and self.canvas.coords(self.rect)[2] > i[0]:
					self.canvas.data["Dir"]['y'] *= -1
					self.canvas.data["Speed"] += 1
					self.canvas.data["yTurn"] = True
					break
			elif i[0] < 10 and self.canvas.data["Dir"]['x'] < 0:
				self.canvas.data["Dir"]['x'] *= -1
				self.canvas.data["xTurn"] = True
				break
			elif i[2] > 490 and self.canvas.data["Dir"]['x'] > 0:
				self.canvas.data["Dir"]['x'] *= -1
				self.canvas.data["xTurn"] = True
				break
			elif i[1] < 10 and self.canvas.data["Dir"]['y'] < 0:
				self.canvas.data["Dir"]['y'] *= -1
				self.canvas.data["yTurn"] = True
				break
				
		if self.canvas.data["xTurn"]:
			self.canvas.data["xTurn"] = False
			self.canvas.coords(self.ball, i[0], i[1], i[2], i[3])
		elif self.canvas.data["yTurn"]:
			self.canvas.data["yTurn"] = False
			self.canvas.coords(self.ball, i[0], i[1], i[2], i[3])
		else:
			self.canvas.move(self.ball, self.canvas.data["Dir"]['x'] * self.canvas.data["Speed"], self.canvas.data["Dir"]['y'] * self.canvas.data["Speed"])
		
		if self.canvas.data["play"]:
			self.root.after(20, self.moveit)
				
	def __init__(self, root):
		self.root = root
		self.canvas = Canvas(root, width=610, height=310)

		self.canvas.pack()
		self.canvas.bind("<Motion>", self.mouseMoved)
		
		self.canvas.data = { }
		self.canvas.data["blockArray"] = []
		self.canvas.data["blockDict"] = {}
		

		for i in range(0,12):
			self.canvas.data["blockDict"][i*40] = {}
			for j in range(0,5):
				self.canvas.data["blockDict"][i*40][j*20 + 40] = [self.canvas.create_rectangle(i*40, j*20+40, i*40 + 40, j*20 + 60, outline='black', fill="orange"), 1]
				
		#print self.canvas.coords( self.canvas.data["blockDict"][0][70][0] )
		
		self.button1 = Button(self.canvas, text = "New game", anchor = W, command = self.new_game)
		self.button1.place(x=500,y=25)
		self.button2 = Button(self.canvas, text = "Quit", anchor = W, command = self.quit)
		self.button2.place(x=570,y=25)
		
		self.ball = self.canvas.create_oval(200, 120, 220, 140, outline='black', fill="black")
		self.rect = self.canvas.create_rectangle(100, 270, 200, 290, outline='black', fill="black")

if __name__ == "__main__":
	root = Tk()
	root.title("BlockBreaker Tk")
	game = game_controller(root);
	root.mainloop()
