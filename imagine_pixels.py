import sys

WIDTH = 512
HEIGHT = 512

PPM_CONFIG = {
    'width': 512,
    'height': 512,
    'max_val': 256,
}

def draw(f):
    for num1 in range(0,512):
        for num2 in range(0,512):
            f.write((str)(num1 / 2 % 256) + " 0 " + (str)(num2 / 2 % 256) + " ")

def main(filename):
    with open(filename, 'w') as f:
        f.write('P3\n{width} {height}\n{max_val}\n'.format(**PPM_CONFIG))
        draw(f)

if __name__ == '__main__':
    if len(sys.argv) < 1:
        print('Please add a filename argument.')
    else:
        main(sys.argv[1])
