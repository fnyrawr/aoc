def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    n_lines = len(lines)
    dict_gears = {}
    sum_numbers = 0
    for i in range(n_lines):  # analyze lines
        num_str = ''
        num_start = -1
        num_end = -1
        linelen = len(lines[i]) - lines[i].count('\n') - lines[i].count('\r')  # remove newline from line length
        for j in range(linelen):
            c = is_digit(lines[i][j])
            if 0 <= c <= 9:  # if digit
                num_str += str(c)  # append char to number
                if num_start < 0:
                    num_start = j  # mark starting position
                if num_start >= 0:
                    num_end = j  # mark ending position
            if not (0 <= c <= 9) or (j == linelen-1):  # if no digit or last char in line
                if num_str != '':
                    # analyze surroundings
                    val = int(num_str.strip())
                    print('analyze {:5} '.format(val), end='')
                    # check same line
                    pos_gear = check_line_sym(lines[i], i, linelen, 0, num_start, num_end)
                    # check line above
                    if (pos_gear is None) and (i > 0):
                        pos_gear = check_line_sym(lines[i-1], i, linelen, -1, num_start, num_end)
                    # check line below
                    if (pos_gear is None) and (i < n_lines-1):
                        pos_gear = check_line_sym(lines[i+1], i, linelen, 1, num_start, num_end)
                    if pos_gear is not None:
                        if pos_gear in dict_gears:
                            dict_gears[pos_gear].append(val)
                        else:
                            dict_gears[pos_gear] = [val]
                    print()
                # reset number
                num_str = ''
                num_start = -1
                num_end = -1
    for entry in dict_gears.values():
        if len(entry) > 1:
            ratio = 1
            for n in entry:
                ratio *= n
            sum_numbers += ratio
    print('Score {:11}'.format(sum_numbers))


def is_digit(char):
    # digits 48 = 0 through 57 = 9
    if 48 <= ord(char) <= 57:
        return int(char)
    return -1


def is_gear(char):
    if ord(char) == 42:
        return True
    return False


def check_line_sym(line, i, k, dir, num_start, num_end):
    char_start = 0
    if num_start > 0:  # get startpoint
        char_start = num_start-1
    char_end = k-1
    if num_end < k-1:  # get endpoint
        char_end = num_end+2
    for j in range(char_start, char_end):
        if is_gear(line[j]):  # if symbol found return True
            print('| found * | i: {:3} | j: {:3}'.format(i+dir, j), end='')
            return str(i+dir) + ',' + str(j)
    return None


if __name__ == '__main__':
    main()