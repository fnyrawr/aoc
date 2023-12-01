def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    sum_values = 0  # sum
    n = 0  # line num for print

    for line in lines:
        n += 1
        k = len(line)-1
        ld = None  # left digit
        for i in range(0, k):
            num = get_number((line[:i]).lower())
            if num:
                ld = num
                break
            if is_digit(line[i]):
                ld = line[i]
                break
        rd = None  # right digit
        for i in range(k, -1, -1):
            num = get_number(line[i:].lower())
            if num:
                rd = num
                break
            if is_digit(line[i]):
                rd = line[i]
                break
        line_val = int(str(ld) + str(rd))
        # print('line {:3}\t{:3}\t{}'.format(n, line_val, line))  # debug
        sum_values += line_val
    print('sum values\t{:3}'.format(sum_values))


def is_digit(char):
    # digits 40 = 0 through 57 = 9
    if 40 <= ord(char) <= 57:
        return True
    return False


def get_number(s):
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }
    if 'one' in s:
        return 1
    if 'two' in s:
        return 2
    if 'three' in s:
        return 3
    if 'four' in s:
        return 4
    if 'five' in s:
        return 5
    if 'six' in s:
        return 6
    if 'seven' in s:
        return 7
    if 'eight' in s:
        return 8
    if 'nine' in s:
        return 9
    if 'zero' in s:
        return 0
    return False


if __name__ == '__main__':
    main()