import sys
import random

WIDTH = 512
HEIGHT = 512
MAX_VAL = 255
COLORS = {
    'blue': '0 0 255',
    'yellow': '255 255 0',
    'red': '255 0 0',
    'white': '255 255 255',
}


def random_color():
    random_num = random.randint(0, 10)
    if random_num > 4:
        if random_num > 8:
            return COLORS['blue']
        elif random_num > 6:
            return COLORS['red']
        return COLORS['yellow']
    return COLORS['white']


def fill_bounds(pixels, x0, y0, x1, y1):
    color = random_color()
    for y in range(y0, y1):
        for x in range(x0, x1):
            pixels[y][x] = color
    pixels[y0][x0] = '0 255 0'
    pixels[y1 - 1][x1 - 1] = '0 255 0'

def draw_bounds(pixels, x0, y0, x1, y1, ornt, i):
    if (i == 4):
        return
    new_ornt = (ornt + 1) % 2
    i += 1
    if ornt == 0:
        q1 = (3 * x0 + x1) / 4
        q3 = (3 * x1 + x0) / 4
        lineX = random.randint(q1, q3)
        # draw on left
        fill_bounds(pixels, x0, y0, lineX - 4, y1)
        draw_bounds(pixels, x0, y0, lineX, y1, new_ornt, i)
        # draw on right
        fill_bounds(pixels, lineX + 4, y0, x1, y1);
        draw_bounds(pixels, lineX, y0, x1, y1, new_ornt, i)
        for y in xrange(y0, y1):
            for x in xrange(lineX - 4, lineX + 4):
                pixels[y][x] = '0 0 0'
    if ornt == 1:
        q1 = (3 * y0 + y1) / 4
        q3 = (3 * y1 + y0) / 4
        lineY = random.randint(q1, q3)
        # draw on top
        fill_bounds(pixels, x0, y0, x1, lineY - 4)
        draw_bounds(pixels, x0, y0, x1, lineY, new_ornt, i)
        # draw on bottom
        fill_bounds(pixels, x0, lineY + 4, x1, y1)
        draw_bounds(pixels, x0, lineY, x1, y1, new_ornt, i)
        for x in xrange(x0, x1):
            for y in xrange(lineY - 4, lineY + 4):
                pixels[y][x] = '0 0 0'


def draw(f):
    pixels = [['255 255 255' for _ in xrange(WIDTH)] for _ in xrange(HEIGHT)]
    draw_bounds(pixels, 0, 0, WIDTH, HEIGHT, 0, 0)
    f.write(' '.join([' '.join(row) for row in pixels]))
    f.write('\n')


def main(filename):
    with open(filename, 'w') as f:
        f.write('P3\n{} {}\n{}\n'.format(WIDTH, HEIGHT, MAX_VAL))
        draw(f)


if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Please add a filename argument.')
    else:
        main(sys.argv[1])
