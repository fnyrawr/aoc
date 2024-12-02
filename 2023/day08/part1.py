def main():
    textfile = 'test_input.txt.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    instructions = [x for x in lines[0] if x != '\n']
    nodes = {}
    for i in range(2, len(lines)):
        nodes[lines[i][0:3]] = [lines[i][7:10], lines[i][12:15]]

    steps = 0
    node = 'AAA'
    while node != 'ZZZ':
        node = walk_sequence(instructions, nodes, node)
        steps += len(instructions)
    print('steps: ' + str(steps))


def walk_sequence(instructions, nodes, node):
    for i in range(len(instructions)):
        if instructions[i] == 'L':
            node = nodes[node][0]
        else:
            node = nodes[node][1]
    return node


if __name__ == '__main__':
    main()