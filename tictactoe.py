import os
from ai import getNextBestMove

class Board:
	def __init__(self, slot1, slot2, slot3, slot4, slot5, slot6, slot7, slot8, slot9, turn):
		self.slot1 = slot1
		self.slot2 = slot2
		self.slot3 = slot3
		self.slot4 = slot4
		self.slot5 = slot5
		self.slot6 = slot6
		self.slot7 = slot7
		self.slot8 = slot8
		self.slot9 = slot9
		self.turn = turn

board = Board('-', '-', '-', '-', '-', '-', '-', '-', '-', 'player')
nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

def tinit():
	createBoard()
	printBoard()
	playerTurn()

def createBoard():
	global board
	board = Board('-', '-', '-', '-', '-', '-', '-', '-', '-', 'player')

def printBoard():
	clear = lambda: os.system('cls')
	#clear()

	global board 
	r1 = '   {s1}  |  {s2}  |  {s3}'.format(s1 = board.slot1, s2 = board.slot2, s3 = board.slot3)
	r2 = '-------------------'
	r3 = '   {s4}  |  {s5}  |  {s6}'.format(s4 = board.slot4, s5 = board.slot5, s6 = board.slot6)
	r4 = '-------------------'
	r5 = '   {s7}  |  {s8}  |  {s9}'.format(s7 = board.slot7, s8 = board.slot8, s9 = board.slot9)

	for x in range(0, 5):
		if x == 0:
			print(r1)
		elif x == 1:
			print(r2)
		elif x == 2:
			print(r3)
		elif x == 3:
			print(r4)
		elif x == 4:
			print(r5)

def getSlot(slot):
	global board 
	slots = list(vars(board))
	for indx, x in enumerate(slots):
		chararray = list(x)
		try:
			if x[4] == str(slot):
				val = x
				return val
		except IndexError:
			break





def modifyBoardSlot(slot, value):
	global board
	orgs = str(getSlot(slot))
	setattr(board, orgs, value)
	swapTurns()

def swapTurns():
	global board 
	if board.turn == 'player':
		board.turn = 'bot'
		printBoard()
		botTurn()
	elif board.turn == 'bot':
		board.turn = 'player'
		printBoard()
		playerTurn()



def playerTurn():
	symbol = input('Please type your slot! You will always be X. (Example: X1 or X5): ')
	symarray = list(symbol)
	if symarray[0] != 'X':
		print('That is not X!')
		playerTurn()

	if ''.join(filter(str.isnumeric, symarray)) in nums:
		modifyBoardSlot(symarray[1], symarray[0])

	print('That is not a valid slot!')
	playerTurn()

def botTurn():
	global board
	move = getNextBestMove(board)
	modifyBoardSlot(move, 'O')


			








