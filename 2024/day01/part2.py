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

    def get_occur_count(y):
        return len([x for x in right_list if x == y])

    for i in range(len(left_list)):
        n = get_occur_count(left_list[i])
        z = n*left_list[i]
        sum_values += z
        print(f"Number {left_list[i]} occurs {n} times -> add {z} sum values: {sum_values}")
    print(f"Sum values: {sum_values}")


if __name__ == '__main__':
    main()