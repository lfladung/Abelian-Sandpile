import time
import sys
import curses
from sys import argv

#Instantiate the curses screen and colors
stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
normalText = curses.A_NORMAL

#Function that will recursively check surrounding cells
def checkSurround(grid, q, w, h):
    if q < h-1 and q > 0 and w < h-1 and w > 0:
         grid[q+1][w] += 1
         if grid[q+1][w] >= 5:
            grid[q+1][w] = 1
            checkSurround(grid,q+1,w,h)
         grid[q][w+1] += 1
         if grid[q][w+1] >= 5:
            grid[q][w+1] = 1
            checkSurround(grid,q,w+1,h)
         grid[q-1][w] += 1
         if grid[q-1][w] >= 5:
            grid[q-1][w] = 1
            checkSurround(grid,q-1,w,h)
         grid[q][w-1] += 1
         if grid[q][w-1] >= 5:
            grid[q][w-1] = 1
            checkSurround(grid,q,w-1,h)
#Initalize color pairs
for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)

#Set of
h = w = 23;
err = False;
window = curses.newwin(h,w,0,0)
Grid = [[0 for y in range(h)] for x in range(w)]

if(len(argv) > 1 and len(argv)-1 %3 != 1):
    i = 1
    for num in range(0, (len(argv) / 3)):
        if(int(argv[i]) > h-1 or int(argv[i+1]) > h-1):
            err = True
        if(int(argv[i]) < 0 or int(argv[i+1]) < 0):
            err = True
        if(int(argv[i+2]) > 4):
            argv[i+2] = 4
        if not err:
            Grid[int(argv[i])][int(argv[i+1])] = int(argv[i+2])
            i += 3
try:
    count = 0
    while True:
        count+=1
        if err:
            break
        Grid[h/2][h/2] += 1
        if Grid[h/2][h/2] == 5:
            Grid[h/2][h/2] = 1
            checkSurround(Grid,h/2,h/2, h)
        time.sleep(.1)

        for x in range(0,w):
            for y in range(0,h):
                if Grid[y][x] == 1:
                    stdscr.addstr(x,y,"%d" % Grid[y][x], curses.color_pair(1))
                elif Grid[y][x] == 2:
                    stdscr.addstr(x,y,"%d" % Grid[y][x], curses.color_pair(2))
                elif Grid[y][x] == 3:
                    stdscr.addstr(x,y,"%d" % Grid[y][x], curses.color_pair(3))
                elif Grid[y][x] == 4:
                    stdscr.addstr(x,y,"%d" % Grid[y][x], curses.color_pair(4))
                elif Grid[y][x] == 0:
                    stdscr.addstr(x,y,"%d" % Grid[y][x], curses.color_pair(5))
            stdscr.refresh()
    curses.endwin()
    print "\nInvalid Parameters"
except KeyboardInterrupt:
    curses.endwin()
    print "\nProgram exited via command"
    print "\n" + str(count) + " grains of sand placed"
