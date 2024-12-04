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
    for i in range(rows):
        for j in range(columns):
            # find horizontal
            if j < columns-3:
                if lines[i][j:j+4] == 'XMAS' or lines[i][j:j+4] == 'SAMX':
                    sum_xmas += 1
            # find vertical
            if i < rows-3:
                if (lines[i][j] == 'X' and lines[i+1][j] == 'M' and lines[i+2][j] == 'A' and lines[i+3][j] == 'S') \
                    or (lines[i][j] == 'S' and lines[i+1][j] == 'A' and lines[i+2][j] == 'M' and lines[i+3][j] == 'X'):
                    sum_xmas += 1
            # find diagonal forward
            if (i < rows-3) and (j < columns-3):
                if (lines[i][j] == 'X' and lines[i+1][j+1] == 'M' and lines[i+2][j+2] == 'A' and lines[i+3][j+3] == 'S') \
                    or (lines[i][j] == 'S' and lines[i+1][j+1] == 'A' and lines[i+2][j+2] == 'M' and lines[i+3][j+3] == 'X'):
                    sum_xmas += 1
            # find diagonal backward
            if i > 2 and j < columns-3:
                if (lines[i][j] == 'X' and lines[i-1][j+1] == 'M' and lines[i-2][j+2] == 'A' and lines[i-3][j+3] == 'S') \
                    or (lines[i][j] == 'S' and lines[i-1][j+1] == 'A' and lines[i-2][j+2] == 'M' and lines[i-3][j+3] == 'X'):
                    sum_xmas += 1
    print(f"total sum = {sum_xmas}")


if __name__ == '__main__':
    main()
