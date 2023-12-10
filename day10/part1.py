"""
    DIRECTIONS | PIPES
    0 UP       | L = up -> right     | | = up -> down
    1 RIGHT    | J = up -> left      | - = left - >right
    2 DOWN     | 7 = left -> down    | . = none
    3 LEFT     | F = right -> down   | S = start
"""


def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    lines = [x.replace('\n', '') for x in lines]  # remove newlines

    starting_pos = None
    pipes = {}
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            # starting position has to be handled different
            if lines[i][j] == 'S':
                starting_pos = (i, j)
                pipe = []
                if (i > 0) and (lines[i-1][j] in ['|', '7', 'F']):
                    pipe.append(0)
                if (j < len(lines[i])) and (lines[i][j+1] in ['-', 'J', '7']):
                    pipe.append(1)
                if (i < len(lines)) and (lines[i+1][j] in ['|', 'L', 'J']):
                    pipe.append(2)
                if (j > 0) and (lines[i][j-1] in ['-', 'L', 'F']):
                    pipe.append(3)
                pipes[i, j] = set_char(pipe)
            else:
                pipes[i, j] = lines[i][j]

    # walk paths from starting position
    pos1 = starting_pos
    pos2 = starting_pos
    dir1 = get_directions(pipes[starting_pos])[0]
    dir2 = get_directions(pipes[starting_pos])[1]
    steps = 0

    while (steps == 0) or (pos1 != pos2):
        pos1 = go_step(pos1, dir1)
        dir1 = get_direction(pipes[pos1], dir1)
        pos2 = go_step(pos2, dir2)
        dir2 = get_direction(pipes[pos2], dir2)
        steps += 1
    print('Steps taken: ' + str(steps))


def go_step(position, direction):
    pos = None
    match direction:
        case 0:
            pos = (position[0]-1, position[1])
        case 1:
            pos = (position[0], position[1]+1)
        case 2:
            pos = (position[0]+1, position[1])
        case 3:
            pos = (position[0], position[1]-1)
    return pos


def get_direction(pipe, direction):
    if pipe == '|':
        if direction == 0:
            return 0
        return 2
    if pipe == '-':
        if direction == 1:
            return 1
        return 3
    if pipe == 'L':
        if direction == 2:
            return 1
        return 0
    if pipe == 'J':
        if direction == 1:
            return 0
        return 3
    if pipe == '7':
        if direction == 1:
            return 2
        return 3
    if pipe == 'F':
        if direction == 0:
            return 1
        return 2


def get_directions(pipe):
    if pipe == '|':
        return [0, 2]
    if pipe == '-':
        return [1, 3]
    if pipe == 'L':
        return [0, 1]
    if pipe == 'J':
        return [0, 3]
    if pipe == '7':
        return [2, 3]
    if pipe == 'F':
        return [1, 2]


def set_char(pipe):
    # store possible directions in array
    match pipe:
        case [0, 2]:
            return '|'
        case [1, 3]:
            return '-'
        case [0, 1]:
            return 'L'
        case [0, 3]:
            return 'J'
        case [2, 3]:
            return '7'
        case [1, 2]:
            return 'F'
        case _:
            return '.'


if __name__ == '__main__':
    main()