import time
import sys
import curses

stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
normalText = curses.A_NORMAL

for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)

h,w = 20,20;
window = curses.newwin(h,w,1,1)
Grid =  [[0 for x in range(w)] for y in range(h)]

def checkSurround(grid, q, w):
    if q < 19 and q >= 0 and w < 19 and w >= 0:
         grid[q+1][w] += 1
         if grid[q+1][w] >= 5:
            grid[q+1][w] = 1
            checkSurround(grid,q+1,w)
         grid[q][w+1] += 1
         if grid[q][w+1] >= 5:
            grid[q][w+1] = 1
            checkSurround(grid,q,w+1)
         grid[q-1][w] += 1
         if grid[q-1][w] >= 5:
            grid[q-1][w] = 1
            checkSurround(grid,q-1,w)
         grid[q][w-1] += 1
         if grid[q][w-1] >= 5:
            grid[q][w-1] = 1
            checkSurround(grid,q,w-1)

while True:
    Grid[9][9] += 1
    if Grid[9][9] == 5:
        Grid[9][9] = 1
        checkSurround(Grid,9,9)

    time.sleep(.05)

    for y in range(0,19):
        for x in range(0,20):
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
        stdscr.addstr(x,y,"\n",normalText)
        stdscr.refresh()
