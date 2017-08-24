import pygame
from  colors import *
import random
import sys
import time


#################################################################
# Class represents playing desk
class Desk(object):

    SHUFFLE_NUMBER = 60 # changing to 200 and higher ruins everything

    def __init__(self, width, height):
        self.matrix =[]
        for i in range(height):
            row = [x + 1 for x in range(i * width, (i+1) * width)]
            self.matrix.append(row)
        self.matrix[height - 1][ width - 1] = 0

    def height(self):
        return len(self.matrix)

    def width(self):
        return len(self.matrix[0])

    def __str__(self):
        str_list = []
        for r in self.matrix:
            for c in r:
                str_list.append(str(c) + "\t")
            str_list.append("\n")
        str_list.pop()
        return "".join(str_list)

    def __eq__(self, other):
        if (self.width() != other.width() or self.height() != other.height()):
            return False
        for r in range(self.height()):
            for c in range(self.width()):
                if self.matrix[r][c] != other.matrix[r][c]:
                    return False;
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.__str__())

    def shuffle(self):
        for i in range(Desk.SHUFFLE_NUMBER):
            self.matrix = self.neighbors()[random.randint(0, len(self.neighbors()) - 1)].matrix

    def get_element(self, row, col):
        return self.matrix[row][col]

    def set_element(self, row, col, value):
        self.matrix[row][col] = value

    def copy(self):
        newDesk = Desk(self.width(), self.height())
        for r in range(self.height()):
            for c in range(self.width()):
                newDesk.set_element(r, c, self.matrix[r][c])
        return newDesk

    def heuristic_cost(self):
        totalSum = 0
        for r in range(self.height()):
            for c in range(self.width()):
                n = self.matrix[r][c] - 1
                if (n == -1):
                    n = self.width() * self.height() - 1
                r_solved = n / self.height()
                c_solved = n % self.width()
                totalSum += abs(r - r_solved)
                totalSum += abs(c - c_solved)
        return totalSum

    def swap(self, r1, c1, r2, c2):
        term = self.matrix[r1][c1]
        self.matrix[r1][c1] = self.matrix[r2][c2]
        self.matrix[r2][c2] = term

    def neighbors(self):
        neighbors = []
        w = self.width()
        h = self.height()
        for r in range(h):
            for c in range(w):
                if (self.matrix[r][c] == 0):
                    if (r != 0):
                        neighbor = self.copy()
                        neighbor.swap(r, c, r - 1, c)
                        neighbors.append(neighbor)
                    if (r != h - 1):
                        neighbor = self.copy()
                        neighbor.swap(r, c, r + 1, c)
                        neighbors.append(neighbor)
                    if (c != 0):
                        neighbor = self.copy()
                        neighbor.swap(r, c, r, c - 1)
                        neighbors.append(neighbor)
                    if (c != w - 1):
                        neighbor = self.copy()
                        neighbor.swap(r, c, r, c + 1)
                        neighbors.append(neighbor)
        return neighbors

# Class represents the game
class Puzzle15(object):

        def __init__(self, width=4, height=4):
            self.desk = Desk(width, height)
            self.desk.shuffle()
            self.steps = 0

        def __str__(self):
            return str(self.desk)

        def __repr__(self):
            return str(self.desk)

        def lowest_score_element(self, openset, score):
            min_score = 2 ** 30
            min_elem = None

            for elem in openset:
                if (elem in score.keys()):
                    if (score[elem] < min_score):
                        min_elem = elem
                        min_score = score[elem]

            return min_elem

        def get_solution(self):
            start = self.desk.copy()
            goal = Desk(self.desk.width(), self.desk.height())

            closed_set = []
            openset = [start]
            came_from = {}

            g_score = {start: 0}
            f_score = {start: g_score[start] + start.heuristic_cost()}

            while len(openset) != 0:
                current = self.lowest_score_element(openset, f_score)
                if (current == goal):
                    return self.reconstruct_path(came_from, current)

                openset.remove(current)
                closed_set.append(current)
                neighbors = current.neighbors()
                for neighbor in neighbors:
                    tentative_g_score = g_score[current] + 1
                    tentative_f_score = tentative_g_score + neighbor.heuristic_cost()

                    if neighbor in closed_set and neighbor in f_score and tentative_f_score >= f_score[neighbor]:
                        continue

                    if neighbor not in openset or (neighbor in f_score and tentative_f_score < f_score[neighbor]):
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score[neighbor] = tentative_f_score
                        if neighbor not in openset:
                            openset.append(neighbor)
                    self.steps += 1
            return None

        def reconstruct_path(self, came_from, current_node):
            if (current_node in came_from):
                p = self.reconstruct_path(came_from, came_from[current_node])
                return p + [current_node]
            else:
                return [current_node]


################################################################

class puzzle_GUI:
    width_window=600
    height_window=680
    row_tile=4
    column_tile=4
    size_tile=80
    fontsize=20
    xposition=(width_window - (size_tile *row_tile+ (row_tile - 1)) )/ 2
    yposition = (height_window - (size_tile *column_tile+ (row_tile - 1)) )/ 2
    #moves=[]
    def drawgame(self,board):
        #self.window.fill(background)
        for tilex in range(board.width()):
            for tiley in range(board.height()):
                top=self.xposition+(self.size_tile*tilex)+(tilex-1)#(tilex-1) to space between square
                left=self.yposition+(self.size_tile*tiley)+(tiley-1)
                pygame.draw.rect(self.window,tilecolor,(left,top,self.size_tile,self.size_tile))
                font = pygame.font.Font('freesansbold.ttf', self.fontsize)
                #board[self.row_tile-1][self.column_tile-1]=''
                Texttile = font.render(str(board.get_element(tilex,tiley)), True, textcolor,tilecolor)
                if board.get_element(tilex,tiley)== 0:
                    pygame.draw.rect(self.window,background, (left, top, self.size_tile, self.size_tile))
                    font = pygame.font.Font('freesansbold.ttf', self.fontsize)
                    #board[self.row_tile - 1][self.column_tile - 1] = ''
                    Texttile = font.render(str(board.get_element(tilex,tiley)), True, background, background)
                self.window.blit(Texttile, (left + self.size_tile / 2, top + self.size_tile / 2))

        pygame.display.update()
    ###########################################



    ##################################################################################


    ################################################################################





    def __init__(self):
        pygame.init()
        
        self.window=pygame.display.set_mode((900,900 ))
        pygame.display.set_caption(' ^^ square puzzle ^^')
        position1 = self.yposition + (4 * 80) + 10
        position2 = self.xposition + (4 * 80) + 10
        font=pygame.font.Font('freesansbold.ttf',self.fontsize)
        surfaceOfFont=font.render('solve',True,Red,White)
        title = font.render('square puzzle ^_^', True, Red, background)

        self.board=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,'']]

        self.window.fill(background)
        pygame.draw.rect(self.window, White, (position2, position1,30, 20))
        self.window.blit(surfaceOfFont,(position2,position1))
        self.window.blit(title, (self.xposition+self.size_tile,30))

        #random.shuffle(self.board)
        puzzle = Puzzle15(4,4)
        solution = puzzle.get_solution()
        print (puzzle.steps)
        for s in solution:

            #for s in range(100000000): print ""
            self.drawgame(s)
            time.sleep(1)
            print (s)
            print


        while True:
            #self.drawgame(self.board)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type ==  pygame.MOUSEBUTTONDOWN:#when click on solve
                    mousex, mousey = event.pos
                    boxRect = pygame.Rect(position2, position1, 30,20)#convert area of rectangle to tuple
                    #print boxRect
                    if boxRect.collidepoint(mousex,mousey):#to check if position belonge to solve position
                        print('ok')#call algorithm




#p=puzzle_GUI()
puzzle = Puzzle15(4, 4)
solution = puzzle.get_solution()
print (puzzle.steps)
for s in solution:
    print (s)
    print

p=puzzle_GUI()