#[File level license goes here]

#I don't know which imports are relevent
import sys
from gi.repository import Gtk
import pygame

import sugar3.activity.activity
import sugargame.canvas

import hfoss

#A class that represents a card in the game.
#Keeps track of the card's position, fraction, and image
#Methods: onClick,onDrag,Draw
class card(object):
	#Initializer for the card class
	#Params:
	#	self - this instance
	#	fraction - the fraction represented by this card
	#	image - an image representation of the card
	def __init__(self,pos,fraction,image):
		self.position = pos
		self.width = 10		#subject to change
		self.height = 50	#subject to change
		
		self.fraction = fraction
		self.image = image
		
		self.beingDragged = false #I need a better name for this
	#Draws the card to the screen
	def draw(canvas):
		#implementation needed

	## MOUSE EVENTS
	#Event handler for when the mouse selects the card
	def onMouseDown(mouse):
		self.beingDragged = true
	#Event handler for when the mouse drags the card
	def onMouseMove(mouse):
		self.position = mouse
	#Event handler for when the card is released
	def onMouseUp(mouse):
		self.beingDragged = true
	
	## HELPER FUNCTIONS
	#Checks if a point is within the card's rectangle
	def pointOnCard(point):
		pos = self.position
		return ((point.x >= pos.x && point.x <= (pos.x + self.width)) &&(point.y >= pos.y && point.y <= (pos.y + self.height))
