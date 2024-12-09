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

    #print(f"Initial disk state: {disk}")

    k = len(disk)-1
    for x in range(id-1):
        # check for each block
        check_id = id-1-x
        #print(f"checking ID {check_id}")
        while disk[k] != check_id:
            k -= 1
        blocksize = 0
        while disk[k-blocksize] == check_id:
            blocksize += 1
        #print(f"blocksize: {blocksize}")

        i = 0
        space = 0
        while i < k:
            if disk[i+space] == check_id:
                break
            while disk[i] != '.':
                i += 1
            space = 1
            while disk[i+space] == '.':
                space += 1
                if i+space >= len(disk):
                    break

            if blocksize <= space:
                for op in range(blocksize):
                    disk[i+op] = disk[k-op]
                    disk[k-op] = '.'
                k = len(disk)-1
                #print(f"disk state after moving {check_id}: {disk}")
                break
            i += space
    # trim disk
    m = len(disk)-1
    while disk[m] == '.':
        m -= 1
    disk = disk[:m+1]
    print(f"final disk stage: {disk}")

    checksum = 0
    for i in range(len(disk)):
        if not disk[i] == '.':
            checksum += i*disk[i]
    print(f"checksum {checksum}")
    # < 6353733529362

if __name__ == '__main__':
    main()