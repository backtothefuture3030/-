import random
import itertools
import time

DIRECTION = list(itertools.product((-1, 0, 1), repeat=2))
DIRECTION.remove((0, 0))


def roach(xsize, ysize, xpos, ypos):
    matrix = {}
    pos = (xpos, ypos)
    count = 0
    while len(matrix) < xsize * ysize:
        matrix[pos] = matrix.get(pos, 0) + 1
        count += 1
        while True:
            tempdir = random.choice(DIRECTION)
            temppos = (pos[0] + tempdir[0], pos[1] + tempdir[1])
            if -1 < temppos[0] < xsize and -1 < temppos[1] < ysize: break
        pos = temppos
    return count, matrix

if __name__ == '__main__':
    t=time.time()
    xsize, ysize, xpos, ypos = 100, 100, 0, 0
    r= roach(xsize,ysize,xpos,ypos)
    print(r[0])
    print(time.time()-t)
    for i in range(ysize):
        print(' '.join(['{0:3}'.format(str(r[1][(j,i)])) for j in range(xsize)]))