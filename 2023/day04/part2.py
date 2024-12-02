def main():
    textfile = 'test_input.txt.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    i = 0
    instances = []
    for k in range(len(lines)):  # init instances array
        instances.append(1)
    for line in lines:
        i += 1
        points = 0
        win_num_s = line.split(':')[1].strip().split('|')[0].strip().split(' ')
        win_num = []
        act_num_s = line.split(':')[1].strip().split('|')[1].strip().split(' ')
        act_num = []

        for num in win_num_s:
            if num != '':  # remove empty numbers
                win_num.append((int(num)))
        for num in act_num_s:
            if num != '':  # remove empty numbers
                act_num.append((int(num)))
        if i > len(instances):
            inst_of = 1
        else:
            inst_of = instances[i-1]
        print('Card ' + str(i), end='')
        print(' | ' + str(inst_of) + ' instances', end='')
        matches = 0
        for num in act_num:
            if num in win_num:
                matches += 1
        print(' | ' + str(matches) + ' matches')
        if matches > 0:
            for k in range(matches):
                # add instances of cards
                instances[i+k] += inst_of
        print('instances ' + str(instances))

    total_cards = 0
    for instance in instances:
        total_cards += instance
    print('Points total {:3}'.format(total_cards))


if __name__ == '__main__':
    main()