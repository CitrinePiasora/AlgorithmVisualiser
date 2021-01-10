from collections import deque
from queue import PriorityQueue
from sys import float_repr_style
from tkinter.constants import FALSE
import pygame

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Breadth First Search Algorithm")

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
	# Function to initialize the visualizer grid
	def __init__(self, row, col, width, total_rows):
		self.row = row
		self.col = col
		self.x = row * width
		self.y = col * width
		self.color = WHITE
		self.neighbors = []
		self.width = width
		self.total_rows = total_rows

	# Returns the position of the currently selected square on the grid
	def get_pos(self):
		return self.row, self.col

	# If the current square on the grid has been visited, color it red
	def is_closed(self):
		return self.color == RED

	# If the current square on the grid is being visited color it green
	def is_open(self):
		return self.color == GREEN

	# If the current square is a barrier/wall color it black
	def is_barrier(self):
		return self.color == BLACK

	# If the current square is the starting point of the search algorithm color it orange
	def is_start(self):
		return self.color == ORANGE

	# If the current square is the end point of the search algorithm color it turquoise
	def is_end(self):
		return self.color == TURQUOISE

	# Function to revert square to its starting color
	def reset(self):
		self.color = WHITE

	# If the current square is the starting point of the search algorithm color it orange
	def make_start(self):
		self.color = ORANGE

	# If the current square on the grid has been visited, color it red
	def make_closed(self):
		self.color = RED

	# If the current square on the grid is being visited color it green
	def make_open(self):
		self.color = GREEN

	# If the current square is a barrier/wall color it black
	def make_barrier(self):
		self.color = BLACK

	# If the current square is the end point of the search algorithm color it turquoise
	def make_end(self):
		self.color = TURQUOISE

	# If the current square is part of the resulting best path color it purple
	def make_path(self):
		self.color = PURPLE

	# Function to draw the screen
	def draw(self, win):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

	# Function that updates the colors of the grid based on the data fed by the algorithm
	def update_neighbors(self, grid):
		self.neighbors = []
		if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_barrier(): # DOWN
			self.neighbors.append(grid[self.row + 1][self.col])

		if self.row > 0 and not grid[self.row - 1][self.col].is_barrier(): # UP
			self.neighbors.append(grid[self.row - 1][self.col])

		if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_barrier(): # RIGHT
			self.neighbors.append(grid[self.row][self.col + 1])

		if self.col > 0 and not grid[self.row][self.col - 1].is_barrier(): # LEFT
			self.neighbors.append(grid[self.row][self.col - 1])

	def __lt__(self, other):
		return False

# Function used to reconstruct the best path found by the algorithm
def reconstruct_path(came_from, current, draw):
	while current in came_from:
		current = came_from[current]
		current.make_path()
		draw()

# Algorithm is contained within this function. This function is the BFS Search Algorithm 
def BFSAlgo(draw, start, end):
	visited = [start]
	queue = [start]
	came_from = {}
	open_set_hash = {start}

	while queue:
		current = queue.pop(0)

		if current == end:
			reconstruct_path(came_from, current, draw)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			if neighbor not in visited:
				came_from[neighbor] = current
				visited.append(neighbor)
				queue.append(neighbor)
				if neighbor not in open_set_hash:
					open_set_hash.add(neighbor)
					neighbor.make_open()
		
		draw()

		if current != False:
			current.make_closed()
	return False

# Function to create the grid that will be used for the search algorithm
def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			spot = Spot(i, j, gap, rows)
			grid[i].append(spot)

	return grid


# Function to draw the grids for the visualizer
def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


# Function to draw the grid
def draw(win, grid, rows, width):
	win.fill(WHITE)

	for row in grid:
		for spot in row:
			spot.draw(win)

	draw_grid(win, rows, width)
	pygame.display.update()


# Returns the row and column value fo the clicked square 
def get_clicked_pos(pos, rows, width):
	gap = width // rows
	y, x = pos

	row = y // gap
	col = x // gap

	return row, col


def h(p1, p2):
	x1, y1 = p1
	x2, y2 = p2
	return abs(x1 - x2) + abs(y1 - y2)

def AStarAlgo(draw, grid, start, end):
	count = 0
	open_set = PriorityQueue()
	open_set.put((0, count, start))
	came_from = {}
	g_score = {spot: float("inf") for row in grid for spot in row}
	g_score[start] = 0
	f_score = {spot: float("inf") for row in grid for spot in row}
	f_score[start] = h(start.get_pos(), end.get_pos())

	open_set_hash = {start}

	while not open_set.empty():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		current = open_set.get()[2]
		open_set_hash.remove(current)

		if current == end:
			reconstruct_path(came_from, end, draw)
			end.make_end()
			return True

		for neighbor in current.neighbors:
			temp_g_score = g_score[current] + 1

			if temp_g_score < g_score[neighbor]:
				came_from[neighbor] = current
				g_score[neighbor] = temp_g_score
				f_score[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
				if neighbor not in open_set_hash:
					count += 1
					open_set.put((f_score[neighbor], count, neighbor))
					open_set_hash.add(neighbor)
					neighbor.make_open()

		draw()

		if current != start:
			current.make_closed()

	return False


def mainAStar(win, width):
	ROWS = 50
	grid = make_grid(ROWS, width)

	start = None
	end = None

	run = True
	while run:
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]: # LEFT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				if not start and spot != end:
					start = spot
					start.make_start()

				elif not end and spot != start:
					end = spot
					end.make_end()

				elif spot != end and spot != start:
					spot.make_barrier()

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()
				if spot == start:
					start = None
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					AStarAlgo(lambda: draw(win, grid, ROWS, width), grid, start, end)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

				if event.key == pygame.K_BACKSPACE:
					import menu
					menu.main_menu()

	pygame.quit()

def mainBFS(win, width):
	# Initialize all the relevant variables
	ROWS = 50
	grid = make_grid(ROWS, width)
	start = None
	end = None
	run = True

	# While program is running
	while run:
		# Draw the screen
		draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			# If the user quits the app, change run to FALSE
			if event.type == pygame.QUIT:
				run = False

			# If user left clicks a square
			if pygame.mouse.get_pressed()[0]: 
				# Gets the position of the users mouse
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]

				# If there is no start and the spot clicked is not the end make start point
				if not start and spot != end:
					start = spot
					start.make_start()

				# If there is no end and the spot clicked is not the start make end point
				elif not end and spot != start:
					end = spot
					end.make_end()

				# If start and end exist and a spot is clicked on, create a barrier
				elif spot != end and spot != start:
					spot.make_barrier()

			# If user right clicks resets the square back to white
			elif pygame.mouse.get_pressed()[2]:
				pos = pygame.mouse.get_pos()
				row, col = get_clicked_pos(pos, ROWS, width)
				spot = grid[row][col]
				spot.reset()

				# if the square is the start, resets the start point
				if spot == start:
					start = None
				# If the square is the end, resets the end point
				elif spot == end:
					end = None

			if event.type == pygame.KEYDOWN:
				# If the space bar is pressed while the start and end points are present
				# Starts the algorithm to search for the best possible path
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for spot in row:
							spot.update_neighbors(grid)

					BFSAlgo(lambda: draw(win, grid, ROWS, width), start, end)
				
				# If the C key is pressed, clears the screen and resets the grid
				if event.key == pygame.K_c:
					start = None
					end = None
					grid = make_grid(ROWS, width)

				if event.key == pygame.K_BACKSPACE:
					import menu
					menu.main_menu()

	pygame.quit()