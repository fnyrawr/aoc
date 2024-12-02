def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    boxes = {}
    for i in range(256):  # init 256 boxes
        boxes[i] = {}
    for line in lines:
        sequence = line.split(',')
        for obj in sequence:
            if '=' in obj:  # add lens
                label = obj.split('=')[0]
                val = int(obj.split('=')[1])
                box = get_hash(label)
                boxes[box][label] = val
            else:  # remove lens
                label = obj.split('-')[0]
                box = get_hash(label)
                if (box in boxes) and (label in boxes[box]):
                    del boxes[box][label]

        # calculate focusing power
        focusing_power = 0
        for i in range(len(boxes)):
            j = 1
            for content in boxes[i]:
                focusing_power += (i+1)*j*boxes[i][content]
                j += 1

        print(focusing_power)


def get_hash(s):
    hash_value = 0
    for c in s:
        hash_value += ord(c)
        hash_value *= 17
        hash_value = hash_value % 256
    return hash_value


if __name__ == '__main__':
    main()