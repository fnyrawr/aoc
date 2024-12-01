def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    sum_values = 0  # sum
    left_list = []  # list left side
    right_list = []  # list right side

    for line in lines:
        s = line.replace('\n', '').split('   ')
        left_list.append(int(s[0]))
        right_list.append(int(s[1]))
    left_list.sort()
    right_list.sort()

    for i in range(len(left_list)):
        diff = abs(left_list[i] - right_list[i])
        sum_values += diff
        print(f"Diff of {left_list[i]} and {right_list[i]} is {diff} -> sum values: {sum_values}")
    print(f"Sum values: {sum_values}")


if __name__ == '__main__':
    main()