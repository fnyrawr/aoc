def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    n_safe = 0  # number of safe reports

    for line in lines:
        levels_orig = [int(x) for x in line.split(' ')]
        k_removed = None
        for k in range(-1, len(levels_orig)):
            safe = True
            levels = levels_orig.copy()
            direction = 0  # 0: not defined, 1: increase, 2: decrease
            if k >= 0:
                k_removed = levels[k]
                del levels[k]
            for i in range(len(levels)-1):
                x = levels[i]
                y = levels[i+1]
                if direction == 0:
                    direction = 1 if x < y else 2 if x > y else 0
                if direction == 0:
                    safe = False
                if x < y and (direction != 1 or y-x > 3):
                    safe = False
                if x > y and (direction != 2 or x-y > 3):
                    safe = False
                if x == y:
                    safe = False
            if safe:
                break
        if safe:
            n_safe += 1
            msg = f"Report {levels_orig} is safe"
            if k_removed:
                msg += f' with level {k_removed} removed'
        else:
            msg = f"report {levels_orig} is unsafe regardless of removed level"
        msg += f" | count safe reports: {n_safe}"
        print(msg)
    print(f"{n_safe} safe reports found")


if __name__ == '__main__':
    main()
