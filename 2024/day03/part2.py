import re


def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    text = ''.join(lines)
    enabled = True
    search = True

    sum_values = 0
    print('Start search')
    while search:
        if enabled:
            if "don't()" in text:
                s = text.split("don't()")[0]
                text = text[len(s):]
            else:
                s = text
                search = False
            print(f"examining section {s}")
            matches = re.findall("mul\\(\\d+,\\d+\\)", s)
            print(f"matches {matches}")
            for match in matches:
                x = match.split('(')[1].split(',')[0]
                y = match.split(')')[0].split(',')[1]
                mul = int(x) * int(y)
                sum_values += mul
                print(f"{x} * {y} = {mul} -> sum {sum_values}")
            enabled = False
            if search:
                print(f"\nremaining text {text}\n")
        else:
            if "do()" in text:
                t = ''.join(text.split("do()")[0])
                text = text[len(t):]
                enabled = True
            else:
                search = False
    print(f"total sum = {sum_values}")


if __name__ == '__main__':
    main()
