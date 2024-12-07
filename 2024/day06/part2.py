def main():
    textfile = 'test_input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    lines = [line.replace('\n', '').strip() for line in lines]

    obstructions = []
    position = None
    direction = 0  # 0: left, 1: up,  2: right, 3: down
    h = len(lines)
    w = len(lines[0])
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == '#':
                obstructions.append((y, x))
            if lines[y][x] in ['<', '^', '>', 'v']:
                position_orig = (y, x)
                direction_orig = 0 if lines[y][x] == '<' else 1 if lines[y][x] == '^' else 2 if lines[y][x] == '>' else 3

    def move(p, d, o=obstructions):
        ypos = p[0]
        xpos = p[1]
        if d == 0:  # left
            p = (ypos, xpos - 1)
            if (ypos, xpos - 2) in o:
                d = 1
        elif d == 1:  # up
            p = (ypos - 1, xpos)
            if (ypos - 2, xpos) in o:
                d = 2
        elif d == 2:  # right
            p = (ypos, xpos + 1)
            if (ypos, xpos + 2) in o:
                d = 3
        else:  # down
            p = (ypos + 1, xpos)
            if (ypos + 2, xpos) in o:
                d = 0
        return p, d

    obstructions_orig = obstructions.copy()

    def test_loop(point):
        obstructions = obstructions_orig.copy()
        obstructions.append(point)
        walked = []
        position = position_orig
        direction = direction_orig
        while 0 <= position[0] < w and 0 <= position[1] < h:
            position, direction = move(position, direction, obstructions)
            if (position, direction) in walked:
                return True
            else:
                walked.append((position, direction))
        return False

    loops = 0
    for j in range(h):
        for i in range(w):
            if test_loop((j, i)):
                loops += 1

    print(f"count loops: {loops}")

if __name__ == '__main__':
    main()