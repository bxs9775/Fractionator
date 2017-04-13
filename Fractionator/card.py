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
		self.fraction = fraction
		self.image = image
	#Event handler for when the mouse selects the card
	def onMouseDown(mouse):
		#implementation needed
	#Event handler for when the mouse drags the card
	def onMouseMove(mouse):
		#implementation needed
	#Event handler for when the card is released
	def onMouseUp(mouse):
		#implementation needed
	#Draws the card to the screen
	def draw(canvas):
		#implementation needed
