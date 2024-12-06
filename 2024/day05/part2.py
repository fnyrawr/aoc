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
        line = lines[i].strip()
        if inst:
            # instructions
            x, y = line.split('|')
            if x in map_orderings:
                map_orderings[x].append(y)
            else:
                map_orderings[x] = [y]
        else:
            # updates
            order = line.split(',')
            order_orig = order.copy()
            # Reorder the list based on the given instructions
            correct = True
            for _ in range(len(order)):  # Retry multiple passes to ensure order
                for j in range(len(order) - 1):
                    if order[j] in map_orderings and order[j + 1] not in map_orderings[order[j]]:
                        order[j], order[j + 1] = order[j + 1], order[j]
                        correct = False
            if not correct:
                # Calculate the middle value after fixing the order
                mid_index = len(order) // 2
                val = int(order[mid_index])
                sum_values += val
                print(f"{order_orig} brought in correct order {order} -> add {val}")
        i += 1
    print(f"total sum = {sum_values}")


if __name__ == '__main__':
    main()