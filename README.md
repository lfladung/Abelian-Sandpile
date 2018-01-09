# Abelian-Sandpile
A small python script that implements a basic Abelian Sandpile model using the curses libary.

You can run this script with:

python sandpile.py

The script is capable of placing preset multiple piles of sand with in the format:

python sandpile.py [x position] [y position] [height]...

Any out of bounds parameters are caught and the script will not run.
Any heights greater than 4 will be set to 4.

BUG: Corners remain 0 after neighbors overflow.
