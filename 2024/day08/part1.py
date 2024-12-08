def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    lines = [line.replace('\n', '').strip() for line in lines]

    antennas = {}
    for i, line in enumerate(lines):
        for j, x in enumerate(line):
            if x != '.':
                frequency = x
                if frequency in antennas:
                    antennas[frequency].append((i, j))
                else:
                    antennas[frequency] = [(i, j)]

    antinodes = set()
    for key in antennas:
        x = antennas[key]
        for i in range(len(x)):
            for j in range(i, len(x)):
                dx = x[i][0] - x[j][0]
                dy = x[i][1] - x[j][1]
                for k in [i, j]:
                    for diff in [(dx, dy), (-dx, -dy)]:
                        ax = x[k][0] + diff[0]
                        ay = x[k][1] + diff[1]
                        if not(ax < 0 or ay < 0 or ax >= len(lines) or ay >= len(lines[ax]) or lines[ax][ay] == key):
                            antinodes.add((ax, ay))

    print(f"{len(antinodes)} unique antinode locations")

if __name__ == '__main__':
    main()