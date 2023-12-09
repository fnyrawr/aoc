def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    history = []
    for line in lines:
        if '\n' in line:  # remove newline character
            line = line[0:len(line)-1]
        values = line.split(' ')  # convert line to str list
        for i in range(len(values)):  # convert to int values
            values[i] = int(values[i])
        values.reverse()
        history.append([values])  # append to history as list to match sublevels later

    history = go_down(history)
    history = go_up(history)
    # print_history(history)
    sum_last_values = 0
    for values in history:
        sum_last_values += values[0][len(values[0])-1]
    print('sum values: ' + str(sum_last_values))


def print_history(history):
    i = 0
    while i < len(history):
        offset = ''
        j = 0
        while j < len(history[i]):
            print(offset + str(history[i][j]))
            offset += '  '
            j += 1
        i += 1


def go_up(history):
    for i in range(len(history)):
        levels = len(history[i])
        j = levels-1
        while j >= 0:
            if j == levels-1:
                history[i][j].append(0)
            else:
                k = history[i][j+1][len(history[i][j+1])-1] + history[i][j][len(history[i][j])-1]
                history[i][j].append(k)
            j -= 1
    return history


def go_down(history):
    for i in range(len(history)):
        # append sublevels to history array
        sublevel = 0
        done = False
        while not done:
            done = False
            values = history[i][sublevel]
            sublevel_values = []
            for k in range(1, len(values)):
                sublevel_values.append(values[k] - values[k-1])
            history[i].append(sublevel_values)
            sublevel += 1
            done = True
            for n in sublevel_values:
                if n != 0:
                    done = False
    return history


if __name__ == '__main__':
    main()