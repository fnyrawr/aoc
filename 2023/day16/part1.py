# DIRECTIONS: 0 up, 1 right, 2 down, 3 left
def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    height = len(lines)-1
    width = len(lines[0])-1
    energized_tiles = [(0, 0)]
    split_tiles = []
    beams = {1: [0, 0, 1]}
    while len(beams) > 0:
        i = 1
        while i <= max(beams):
            # placeholder for new beam if splitter hit
            pos_x_n = None
            pos_y_n = None
            direction_n = None
            if i in beams:
                # get position and direction
                pos_x = beams[i][1]
                pos_y = beams[i][0]
                direction = beams[i][2]
                char = lines[pos_y][pos_x]
                if char == '.':
                    pos_y, pos_x, direction = move_beam(pos_y, pos_x, direction)
                if char == '|':
                    if direction in [0, 2]:
                        pos_y, pos_x, direction = move_beam(pos_y, pos_x, direction)
                    else:
                        if (pos_y, pos_x) not in split_tiles:
                            split_tiles.append((pos_y, pos_x))
                            pos_y_n, pos_x_n, direction_n = pos_y, pos_x, 0
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 2)
                        else:
                            pos_y, pos_x, direction = -1, -1, 2
                if char == '-':
                    if direction in [1, 3]:
                        pos_y, pos_x, direction = move_beam(pos_y, pos_x, direction)
                    else:
                        if (pos_y, pos_x) not in split_tiles:
                            split_tiles.append((pos_y, pos_x))
                            pos_y_n, pos_x_n, direction_n = pos_y, pos_x, 3
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 1)
                        else:
                            pos_y, pos_x, direction = -1, -1, 2
                if char == '/':
                    match direction:
                        case 0:
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 1)
                        case 1:
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 0)
                        case 2:
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 3)
                        case 3:
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 2)
                if char == '\\':
                    match direction:
                        case 0:
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 3)
                        case 1:
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 2)
                        case 2:
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 1)
                        case 3:
                            pos_y, pos_x, direction = move_beam(pos_y, pos_x, 0)
                beams[i] = [pos_y, pos_x, direction]
            if pos_x_n is not None:
                beams[max(beams)+1] = [pos_y_n, pos_x_n, direction_n]
            i += 1
        for k in range(1, max(beams)+1):
            if k in beams:
                pos_x = beams[k][1]
                pos_y = beams[k][0]
                if (pos_y < 0) or (pos_y > height) or (pos_x < 0) or (pos_x > width):
                    del beams[k]
                else:
                    if (pos_y, pos_x) not in energized_tiles:
                        energized_tiles.append((pos_y, pos_x))
            k += 1
        # print(beams)
        # print(split_tiles)
    # for y in range(height+1):
    #     for x in range(width+1):
    #         if (y, x) in energized_tiles:
    #             print('#', end='')
    #         else:
    #             print(lines[y][x], end='')
    #     print()
    print(str(len(energized_tiles)) + ' tiles become energized')


def move_beam(pos_y, pos_x, direction):
    if direction == 0:
        return pos_y-1, pos_x, 0
    if direction == 1:
        return pos_y, pos_x+1, 1
    if direction == 2:
        return pos_y+1, pos_x, 2
    if direction == 3:
        return pos_y, pos_x-1, 3


if __name__ == '__main__':
    main()
