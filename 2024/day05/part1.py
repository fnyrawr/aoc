def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    # ordering instructions
    i = 0
    inst = True
    map_orderings = {}
    sum_values = 0
    while i < len(lines):
        if lines[i] == '\n':
            inst = False
            i += 1
            continue
        line = lines[i].replace('\n', '').strip()
        if inst:
            # instructions
            x = line.split('|')[0]
            y = line.split('|')[1]
            if x in map_orderings:
                map_orderings[x].append(y)
            else:
                map_orderings[x] = [y]
        else:
            # updates
            order = line.split(',')
            correct = True
            for j in range(len(order)-1):
                if (order[j] not in map_orderings) or (not order[j+1] in map_orderings[order[j]]):
                    correct = False
            if correct:
                val = int(order[int(len(order) / 2)])
                sum_values += val
                print(f"{order} is in correct order -> add {val}")
        i += 1

    #print(map_orderings)
    print(f"total sum = {sum_values}")


if __name__ == '__main__':
    main()