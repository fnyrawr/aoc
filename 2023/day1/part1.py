def main():
    textfile = 'test_input.txt.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    sum_values = 0  # sum
    n = 0  # line num for print

    for line in lines:
        n += 1
        k = len(line)-1
        ld = None  # left digit
        for i in range(0, k):
            if is_digit(line[i]):
                ld = line[i]
                break
        rd = None  # right digit
        for i in range(k, -1, -1):
            if is_digit(line[i]):
                rd = line[i]
                break
        line_val = int(str(ld) + str(rd))
        # print('line {:3}\t{:3}\t{}'.format(n, line_val, line))  # debug
        sum_values += line_val
    print('sum values\t{:3}'.format(sum_values))


def is_digit(char):
    # digits 48 = 0 through 57 = 9
    if 48 <= ord(char) <= 57:
        return True
    return False


if __name__ == '__main__':
    main()