def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        line = ''.join(file.readlines()).replace('\n', '').strip()

    disk = []
    id = 0
    for i in range(len(line)):
        k = int(line[i])
        if i%2 == 0:
            for l in range(k):
                disk.append(id)
            id += 1
        else:
            for l in range(k):
                disk.append('.')

    i = 0
    k = len(disk)-1
    while i < k:
        i += 1
        if disk[i] == '.':
            while disk[k] == '.':
                k -= 1
            disk[i] = disk[k]
            disk[k] = '.'
            k -= 1
    if disk[i-1] == '.' and disk[i] != '.':
        disk[i-1] = disk[i]
        disk[i] = '.'
    disk = disk[:i]

    checksum = 0
    for i in range(len(disk)):
        if disk[i] == '.':
            break
        checksum += i*disk[i]

    print(f"checksum {checksum}")

if __name__ == '__main__':
    main()