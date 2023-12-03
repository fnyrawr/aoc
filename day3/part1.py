def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    n_lines = len(lines)
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
                    valid = check_line_sym(lines[i], linelen, num_start, num_end)
                    # check line above
                    if not valid and (i > 0):
                        valid = check_line_sym(lines[i-1], linelen, num_start, num_end)
                    # check line below
                    if not valid and (i < n_lines-1):
                        valid = check_line_sym(lines[i+1], linelen, num_start, num_end)
                    if valid:
                        sum_numbers += val
                        print(' | score: {:7}'.format(sum_numbers), end='')
                    print()
                # reset number
                num_str = ''
                num_start = -1
                num_end = -1
    print('Score {:11}'.format(sum_numbers))


def is_digit(char):
    # digits 48 = 0 through 57 = 9
    if 48 <= ord(char) <= 57:
        return int(char)
    return -1


def is_symbol(char):
    if (is_digit(char) > -1) or (ord(char) == 46):
        return False
    print(char, end='')
    return True


def check_line_sym(line, k, num_start, num_end):
    char_start = 0
    if num_start > 0:  # get startpoint
        char_start = num_start-1
    char_end = k-1
    if num_end < k-1:  # get endpoint
        char_end = num_end+2
    s = line[char_start:char_end]
    for c in s:
        if is_symbol(c):  # if symbol found return True
            return True
    return False


if __name__ == '__main__':
    main()