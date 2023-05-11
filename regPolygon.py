import math
from re import A
import turtle

class RegPolygon:
	
	# Used for drawing the polygon
	PIXEL_SIZE = 100
	
	# object initializer or constructor
	# @param numSides the number of sides of in the regular polygon   
	# Precondition: numSides must be a positive integer greater than 2 
	# Postcondition: sets numSides to the correct value based on the parameter numSides
	# 				 sets remaining object variables to zero
	def __init__(self, numSides):
		self.numSides = numSides
		self.sideLength = 0
		self.apothem = 0
		self.radius = 0
	
	# object string representation 		
	def __str__(self):
		info =  '{0: <18}'.format('Number of sides ') + '= ' + str(self.numSides) +'\n'
		info += '{0: <18}'.format('Side Length ') + '= ' + str(self.sideLength) + '\n'
		info += '{0: <18}'.format('Apothem ') + '= ' + str(self.apothem) + '\n'
		info += '{0: <18}'.format('Radius ') + '= ' + str(self.radius) + '\n'
		info += '{0: <18}'.format('Perimeter ') + '= ' + str(self.perimeter()) + '\n'
		info += '{0: <18}'.format('Area ') + '= ' + str(self.area()) + '\n'
		
		return info
			
	# @param sideLength the length of a side 
	# Precondition: sideLength is a positive real number
	# Postcondition: sets sideLength, apothem and radius to the correct values based on 
	#				 the parameter sideLength
	def setSide(self,sideLength):
		self.sideLength = sideLength
		A = (math.pi * (self.numSides-2)) / (2*(self.numSides))
		self.apothem = (sideLength*math.tan(A))/2
		self.radius = sideLength/(2*math.cos(A))
		
		
		
	
	# @param apothem the length of the apothem 
	# Precondition: apothem is a positive real number
	# Postcondition: sets apothem, sideLength and radius to the correct values based on 
	#				 the parameter apothem
	def setApothem(self,apothem):
		self.apothem = apothem
		A = (math.pi* (self.numSides-2)) / (2*(self.numSides))
		self.sideLength = (2*apothem)/(math.tan(A))
		self.radius = apothem/(math.sin(A))
		
		
	
	# @param radius the length of the radius 
	# Precondition: radius is a positive real number
	# Postcondition: sets radius, apothem, and sideLength to the correct values based on 
	#				 the parameter radius
	def setRadius(self, radius):
		self.radius = radius
		A = (math.pi* (self.numSides-2)) / (2*(self.numSides))
		self.sideLength = radius*(math.sin(A))
		self.apothem = (2*radius)*(math.cos(A))

		
	
	# Postcondition: returns the perimeter 	
	def perimeter(self):
		return (self.numSides * self.sideLength)
		
		
			
	
	# Postcondition: returns the area	
	def area(self):
		return (0.5 * self.numSides * self.apothem * self.sideLength)
		
		
		
	
	############ EXTRA CREDIT ONLY ###############
	# using the python turtle package, draws the regular polygon and also 
	# displays all relevant info
	#def draw(self):
		
		

