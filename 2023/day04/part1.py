def main():
    textfile = 'test_input.txt.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    sum_points = 0
    i = 0
    for line in lines:
        i += 1
        points = 0
        win_num_s = line.split(':')[1].strip().split('|')[0].strip().split(' ')
        win_num = []
        act_num_s = line.split(':')[1].strip().split('|')[1].strip().split(' ')
        act_num = []
        print(line.split(':')[1].strip().split('|')[0].strip().split(' '))
        print('win num: ' + str(win_num))
        print('act num: ' + str(act_num))
        for num in win_num_s:
            if num != '':  # remove empty numbers
                win_num.append((int(num)))
        for num in act_num_s:
            if num != '':  # remove empty numbers
                act_num.append((int(num)))
        for num in act_num:
            if num in win_num:
                print(str(i) + ' found ' + str(num))
                points = 1 if (points == 0) else points*2
        sum_points += points
        print(str(i) + ' ' + str(points))

    print('Points total {:3}'.format(sum_points))


if __name__ == '__main__':
    main()