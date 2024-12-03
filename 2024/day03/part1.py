import re

def main():
    textfile = 'test_input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    sum_values = 0
    print(lines[0])
    matches = re.findall("mul\\(\\d+,\\d+\\)", lines[0])
    for match in matches:
        x = match.split('(')[1].split(',')[0]
        y = match.split(')')[0].split(',')[1]
        sum_values += int(x)*int(y)
    print(matches)


if __name__ == '__main__':
    main()