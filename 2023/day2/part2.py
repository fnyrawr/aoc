def main():
    textfile = 'test_input.txt.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    max_r = 12
    max_g = 13
    max_b = 14

    score = 0
    i = 0
    for line in lines:
        cubeset = get_cubesets(line)
        red = cubeset['red']
        green = cubeset['green']
        blue = cubeset['blue']
        power = red * green * blue
        score += power
        print('{:3}   possible | {:2} red | {:2} green | {:2} blue | power {:5}'.format(i, red, green, blue, power))
    print('Score: {:5}'.format(score))


# get total of cubes used
def get_cubesets(line):
    cubes = {}  # return dict with cubesets
    cubesets = line.split(':')[1].split(';')
    red = 0
    green = 0
    blue = 0
    for cubeset in cubesets:
        subsets = cubeset.split(',')
        for subset in subsets:  # get max cubes in each game
            if 'red' in subset:
                r = int(subset[1:].split(' ')[0])
                if (red == 0) or ((r > 0) and (r > red)):
                    red = r
            if 'green' in subset:
                g = int(subset[1:].split(' ')[0])
                if (green == 0) or ((g > 0) and (g > green)):
                    green = g
            if 'blue' in subset:
                b = int(subset[1:].split(' ')[0])
                if (blue == 0) or ((b > 0) and (b > blue)):
                    blue = b
    cubes['red'] = red
    cubes['green'] = green
    cubes['blue'] = blue
    return cubes


if __name__ == '__main__':
    main()