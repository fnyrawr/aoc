def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    sum_values = 0  # sum
    left_list = []  # list left side
    right_list = []  # list right side
    num_counts = {}  # dict of number occurences

    for line in lines:
        s = line.replace('\n', '').split('   ')
        left_list.append(int(s[0]))
        right_list.append(int(s[1]))
    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        if left_list[i] in num_counts:
            n = num_counts[left_list[i]]
        else:
            n = right_list.count(left_list[i])
            num_counts[left_list[i]] = n
        z = n*left_list[i]
        sum_values += z
        print(f"Number {left_list[i]} occurs {n} times -> add {z} sum values: {sum_values}")
    print(f"Sum values: {sum_values}")


if __name__ == '__main__':
    main()
