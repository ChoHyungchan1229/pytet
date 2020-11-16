from matrix import *
import random

def draw_matrix(m):
    array = m.get_array()
    for y in range(m.get_dy()):
        for x in range(m.get_dx()):
            if array[y][x] == 0:
                print("□", end='')
            elif array[y][x] == 1:
                print("■", end='')
            else:
                print("XX", end='')
        print()

def rotate_right(m):
	array = m.get_array()
	dy = m.get_dy()
	dx = m.get_dx()
	tmp = [[0 for i in range(dx)] for j in range (dy)]
	for y in range(dy):
		for x in range(dx):
			tmp[x][y] = array[dy-y-1][x]
	
	return tmp

def rotate_left(m):
	array = m.get_array()
	dy = m.get_dy()
	dx = m.get_dx()
	tmp = [[0 for i in range(dx)] for j in range (dy)]
	for y in range(dy):
		for x in range(dx):
			tmp[x][y] = array[y][dx-x-1]
	
	return tmp

###
### initialize variables
###     
arrayBlk =[ [ [1, 1], [1, 1] ], [ [0, 0, 1], [1, 1, 1], [0, 0, 0] ], [ [1, 0, 0], [1, 1, 1], [0, 0, 0] ], [ [0, 1, 0], [1, 1, 1], [0, 0, 0] ], [ [0, 1, 1], [1, 1, 0], [0, 0, 0] ], [ [1, 1, 0], [0, 1, 1], [0, 0, 0] ], [ [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ], [ 0, 0, 1, 0 ] ] ]

### integer variables: must always be integer!
iScreenDy = 15
iScreenDx = 10
iScreenDw = 4
top = 0
left = iScreenDw + iScreenDx//2 - 2

newBlockNeeded = False

arrayScreen = [
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
    [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ] ]

###
### prepare the initial screen output
###  
iScreen = Matrix(arrayScreen)
oScreen = Matrix(iScreen)
a = random.randrange(0, 6)
currBlk = Matrix(arrayBlk[a])
tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
tempBlk = tempBlk + currBlk
oScreen.paste(tempBlk, top, left)
draw_matrix(oScreen); print()

###
### execute the loop
###

while True:
	key = input('Enter a key from [ q (quit), a (left), d (right), s (down), w (rotate), \' \' (drop) ] : ')
	if key == 'q':
		print('Game terminated...')
		break
	elif key == 'a': # move left
		left -= 1
	elif key == 'd': # move right
		left += 1
	elif key == 's': # move down
		top += 1
	elif key == 'w': # rotate the block clockwise
		currBlk = rotate_right(currBlk)
		currBlk = Matrix(currBlk)	
	elif key == ' ': # drop the block
		while True:
			top += 1
			tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
			tempBlk = tempBlk + currBlk
			if tempBlk.anyGreaterThan(1):
				break
	else:
	   print('Wrong key!!!')
	   continue

	# collsion TEST-------------------------
	tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
	tempBlk = tempBlk + currBlk
	if tempBlk.anyGreaterThan(1):
		if key == 'a': # undo: move right
			left += 1
		elif key == 'd': # undo: move left
			left -= 1
		elif key == 's': # undo: move up
			top -= 1
			newBlockNeeded = True
		elif key == 'w': # undo: rotate the block counter-clockwise
			currBlk = rotate_left(currBlk)
			currBlk = Matrix(currBlk)
			print('Impossible')
		elif key == ' ': # undo: move up
			top -= 1
			newBlockNeeded = True

		tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
		tempBlk = tempBlk + currBlk
	#---------------------------------
	oScreen = Matrix(iScreen)
	oScreen.paste(tempBlk, top, left)
	draw_matrix(oScreen); print()

	#----NEW BLOCK----
	if newBlockNeeded:
		iScreen = Matrix(oScreen)
		top = 0
		left = iScreenDw + iScreenDx//2 - 2
		newBlockNeeded = False
		#테트리스 모양 랜덤 설정
		a = random.randrange(0, 6)
		currBlk = Matrix(arrayBlk[a])
		
		tempBlk = iScreen.clip(top, left, top+currBlk.get_dy(), left+currBlk.get_dx())
		tempBlk = tempBlk + currBlk
		if tempBlk.anyGreaterThan(1):
			print('Game Over!!!')
			break
        
		oScreen = Matrix(iScreen)
		oScreen.paste(tempBlk, top, left)
		draw_matrix(oScreen); print()
        
###
### end of the loop
###
