def main():
    textfile = 'input.txt'
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
                position = (y, x)
                direction = 0 if lines[y][x] == '<' else 1 if lines[y][x] == '^' else 2 if lines[y][x] == '>' else 3

    visited = []

    def move(p, d):
        ypos = p[0]
        xpos = p[1]
        if d == 0:  # left
            p = (ypos, xpos-1)
            if (ypos, xpos-2) in obstructions:
                d = 1
        elif d == 1:  # up
            p = (ypos-1, xpos)
            if (ypos-2, xpos) in obstructions:
                d = 2
        elif d == 2:  # right
            p = (ypos, xpos+1)
            if (ypos, xpos+2) in obstructions:
                d = 3
        else:  # down
            p = (ypos+1, xpos)
            if (ypos+2, xpos) in obstructions:
                d = 0
        return p, d

    while 0 <= position[0] < w and 0 <= position[1] < h:
        position, direction = move(position, direction)
        if position not in visited:
            visited.append(position)

    print(f"{len(visited)} unique positions")

if __name__ == '__main__':
    main()