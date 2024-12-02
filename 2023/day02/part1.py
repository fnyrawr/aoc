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
        i += 1
        cubeset = get_cubesets(line)
        red = cubeset['red']
        green = cubeset['green']
        blue = cubeset['blue']
        if (red <= max_r) and (green <= max_g) and (blue <= max_b):
            score += i
            print('{:3}   possible | {:2} red | {:2} green | {:2} blue | score {:5}'.format(i, red, green, blue, score))
        else:
            print('{:3} impossible | {:2} red | {:2} green | {:2} blue'.format(i, red, green, blue))
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
                if r > red:
                    red = r
            if 'green' in subset:
                g = int(subset[1:].split(' ')[0])
                if g > green:
                    green = g
            if 'blue' in subset:
                b = int(subset[1:].split(' ')[0])
                if b > blue:
                    blue = b
    cubes['red'] = red
    cubes['green'] = green
    cubes['blue'] = blue
    return cubes


if __name__ == '__main__':
    main()