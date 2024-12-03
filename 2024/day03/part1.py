import re


def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    sum_values = 0
    matches = re.findall("mul\\(\\d+,\\d+\\)", ''.join(lines))
    print(matches)
    for match in matches:
        x = match.split('(')[1].split(',')[0]
        y = match.split(')')[0].split(',')[1]
        mul = int(x)*int(y)
        sum_values += mul
        print(f"{x} * {y} = {mul} -> sum {sum_values}")
    print(f"total sum = {sum_values}")


if __name__ == '__main__':
    main()
