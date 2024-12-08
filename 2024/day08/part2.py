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

                for k in range(len(lines)):
                    out_of_bounds = 0
                    for diff in [(dx, dy), (-dx, -dy)]:
                        ax = x[i][0] + diff[0] * k
                        ay = x[i][1] + diff[1] * k

                        if not(ax < 0 or ay < 0 or ax >= len(lines) or ay >= len(lines[ax])):
                            antinodes.add((ax, ay))
                            continue
                        out_of_bounds += 1

                    if out_of_bounds == 2:
                        break

    print(f"{len(antinodes)} unique antinode locations")


if __name__ == "__main__":
    main()