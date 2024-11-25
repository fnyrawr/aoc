def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    hash_values = []
    for line in lines:
        sequence = line.split(',')
        for obj in sequence:
            hash_values.append(get_hash(obj))
    print(sum(hash_values))


def get_hash(s):
    hash_value = 0
    for c in s:
        hash_value += ord(c)
        hash_value *= 17
        hash_value = hash_value % 256
    return hash_value


if __name__ == '__main__':
    main()