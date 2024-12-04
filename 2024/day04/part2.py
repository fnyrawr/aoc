def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    # clean
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '').strip()

    sum_xmas = 0
    rows = len(lines)
    columns = len(lines[0])
    for i in range(rows-2):
        for j in range(columns-2):
            # find X-MAS patterns
            if (lines[i][j] == 'M' and lines[i][j+2] == 'M' and lines[i+2][j] == 'S' and lines[i+2][j+2] == 'S' and lines[i+1][j+1] == 'A') \
                or (lines[i][j] == 'M' and lines[i][j+2] == 'S' and lines[i+2][j] == 'M' and lines[i+2][j+2] == 'S' and lines[i+1][j+1] == 'A') \
                or (lines[i][j] == 'S' and lines[i][j+2] == 'M' and lines[i+2][j] == 'S' and lines[i+2][j+2] == 'M' and lines[i+1][j+1] == 'A') \
                or (lines[i][j] == 'S' and lines[i][j+2] == 'S' and lines[i+2][j] == 'M' and lines[i+2][j+2] == 'M' and lines[i+1][j+1] == 'A'):
                sum_xmas += 1
    print(f"total sum = {sum_xmas}")


if __name__ == '__main__':
    main()