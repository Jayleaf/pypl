from inspect import Attribute
import json
import random
from select import select


nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
movelist = 'hi'
boardS = ''
step = 0

def getNextBestMove(board):
	global step
	global boardS
	boardS = board
	f = open('./aidata.json')
	global movelist
	movelist = json.load(f).get('Wins') # Loads the JSON that's full of the possible winning movesets

	if shouldPlayDefense() != False:
		print(shouldPlayDefense())
		return shouldPlayDefense()

	if returnNextLegalMoveWithAChanceToWin(movelist) != False: # Checks to see if there is a possible legal move with a winning chance
		nlm = returnNextLegalMoveWithAChanceToWin(movelist) # if so, set it to a variable, increase step, and return.
		step = step + 1
		return nlm
	else:
		for x in range(0, 10):
			selection = random.choice(nums)					# this code will, if there is no move with winning chance, choose a random place to input it's O.
			if isMoveLegal('O' + selection) == True:
				return selection
			else:
				nums.remove(selection)


def returnNextLegalMoveWithAChanceToWin(sets): # the sets that this takes in is the list of every possible winning combination (from the json.)
	global step
	global boardS
	newsets = sets
	for set in newsets: # for each set in the list of winning sets
		move = set.split(',') # split the set into each individual move
		if isMoveLegal('O' + list(move[0])[1]) == False or isMoveLegal('O' + list(move[1])[1]) == False or isMoveLegal('O' + list(move[2])[1]) == False: #if any move in the set is illegal
			step = 0 #reset the step counter
			continue #continue to the next set
		else: #if the set is legal
			return list(move[step])[1] #make the next move according to the step we're on
	return False #will return false if no sets moves remain.


def isMoveLegal(move):
	global boardS
	board = boardS
	movearr = list(move)
	from tictactoe import getSlot
	slotval = getSlot(movearr[1])
	sym = getattr(board, slotval)
	if sym == '-':
		return True
	else:
		return False

		
def shouldPlayDefense():
	global boardS
	board = boardS

	# this doesn't really work. You'd have to hard-code checks for each slot. Have fun :)

	for x in range(1, 10):
		from tictactoe import getSlot
		slot = getSlot(x)
		if getattr(board, slot) == 'X':
			try:
				if getattr(board, getSlot(str(x + 1))) == '-': # checks right slot
					return list(getSlot(str(x+1)))[4]		
				if getattr(board, str(getSlot(str(x - 1)))) == '-': # checks left slot
					return list(getSlot(str(x-1)))[4]
				if getattr(board, str(getSlot(str(x + 3)))) == '-': # checks below slot
					return list(getSlot(str(x + 3)))[4]
				if getattr(board, str(getSlot(str(x - 3)))) == '-': # checks above slot
					return list(getSlot(str(x-3)))[4]
				if getattr(board, str(getSlot(str(x + 4)))) == '-': # checks above diagonal
					return list(getSlot(str(x+4)))[4]					
				if getattr(board, str(getSlot(str(x - 4)))) == '-': # checks below diagonal
					return list(getSlot(str(x-4)))[4]
				return False
			except:
				try:	
					if getattr(board, str(getSlot(str(x - 1)))) == '-': # checks left slot
						return list(getSlot(str(x-1)))[4]
					if getattr(board, str(getSlot(str(x + 3)))) == '-': # checks below slot
						return list(getSlot(str(x + 3)))[4]
					if getattr(board, str(getSlot(str(x - 3)))) == '-': # checks above slot
						return list(getSlot(str(x-3)))[4]
					if getattr(board, str(getSlot(str(x + 4)))) == '-': # checks above diagonal
						return list(getSlot(str(x+4)))[4]					
					if getattr(board, str(getSlot(str(x - 4)))) == '-': # checks below diagonal
						return list(getSlot(str(x-4)))[4]
					return False
				except:
					try:	
						if getattr(board, str(getSlot(str(x + 3)))) == '-': # checks below slot
							return list(getSlot(str(x + 3)))[4]
						if getattr(board, str(getSlot(str(x - 3)))) == '-': # checks above slot
							return list(getSlot(str(x-3)))[4]
						if getattr(board, str(getSlot(str(x + 4)))) == '-': # checks above diagonal
							return list(getSlot(str(x+4)))[4]					
						if getattr(board, str(getSlot(str(x - 4)))) == '-': # checks below diagonal
							return list(getSlot(str(x-4)))[4]
						return False
					except:
						try:	
							if getattr(board, str(getSlot(str(x - 3)))) == '-': # checks above slot
								return list(getSlot(str(x-3)))[4]
							if getattr(board, str(getSlot(str(x + 4)))) == '-': # checks above diagonal
								return list(getSlot(str(x+4)))[4]					
							if getattr(board, str(getSlot(str(x - 4)))) == '-': # checks below diagonal
								return list(getSlot(str(x-4)))[4]
							return False
						except:
							try:	
								if getattr(board, str(getSlot(str(x + 4)))) == '-': # checks above diagonal
									return list(getSlot(str(x+4)))[4]					
								if getattr(board, str(getSlot(str(x - 4)))) == '-': # checks below diagonal
									return list(getSlot(str(x-4)))[4]
								return False
							except:
								try:					
									if getattr(board, str(getSlot(str(x - 4)))) == '-': # checks below diagonal
										return list(getSlot(str(x-4)))[4]
									return False
								except:
									return False


