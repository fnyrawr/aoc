import math

def main():
    textfile = 'test_input.txt.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    instructions = [x for x in lines[0] if x != '\n']
    nodes = {}
    for i in range(2, len(lines)):
        nodes[lines[i][0:3]] = [lines[i][7:10], lines[i][12:15]]

    positions = [x for x in nodes if x[2] == 'A']
    print('starting points: ' + str(positions))
    results = []
    for node in positions:
        steps = 0
        while node[2] != 'Z':
            node = walk_sequence(instructions, nodes, node)
            steps += len(instructions)
        results.append(steps)
    print('results: ' + str(results))
    lcm = math.lcm(*results)
    print('steps: ' + str(lcm))


def walk_sequence(instructions, nodes, node):
    for i in range(len(instructions)):
        if instructions[i] == 'L':
            node = nodes[node][0]
        else:
            node = nodes[node][1]
    return node


if __name__ == '__main__':
    main()