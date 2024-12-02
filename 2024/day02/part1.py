def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    n_safe = 0  # number of safe reports

    for line in lines:
        levels = [int(x) for x in line.split(' ')]
        direction = 0  # 0: not defined, 1: increase, 2: decrease
        safe = True
        for i in range(len(levels)-1):
            x = levels[i]
            y = levels[i+1]
            if direction == 0:
                direction = 1 if x < y else 2 if x > y else 0
            if direction == 0:
                safe = False
                break
            if x < y and (direction != 1 or y-x > 3):
                safe = False
                break
            if x > y and (direction != 2 or x-y > 3):
                safe = False
                break
            if x == y:
                safe = False
                break
        if safe:
            n_safe += 1
        print(f"Report {levels} is {'safe' if safe else 'unsafe'}")
    print(f"{n_safe} safe reports found")


if __name__ == '__main__':
    main()