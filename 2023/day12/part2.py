def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if '\n' in lines[i]:  # remove newline characters
            lines[i] = lines[i][:len(lines[i]) - 1]

    springs = []
    groups = []
    for i in range(len(lines)):
        springs.append(lines[i].split(' ')[0])
        springs[i] = "?".join(5 * [springs[i]])
        groups.append(lines[i].split(' ')[1].split(','))
        groups[i] = [int(x) for x in groups[i]]
        groups[i] = 5*groups[i]

    sum_total = 0
    for i in range(len(lines)):
        clusters = get_clusters(springs[i])
        combinations = get_combinations(groups[i], clusters)
        sum_total += combinations
    print('Possibilities total: ' + str(sum_total))


def get_clusters(springs):
    return [s for s in springs.split('.') if s]


def get_combinations(groups, clusters, cache={}):
    key = "|".join(map(str, groups))
    key += "#" + ":".join(clusters)
    if key in cache:
        return cache[key]

    if not groups:
        for cluster in clusters:
            if "#" in cluster:
                return 0
        return 1
    if not clusters:
        return 0

    ret = 0
    group = groups[0]
    cluster = clusters[0]

    if group > len(cluster) and "#" in cluster:
        return 0

    for i in range(len(cluster) - group + 1):
        left = cluster[:i]
        if "#" in left:
            continue
        right = cluster[i + group:]
        if right.startswith("#"):
            continue
        new_clusters = clusters[1:]
        if len(right) > 1:
            new_clusters.insert(0, right[1:])
        ret += get_combinations(groups[1:], new_clusters, cache)

    if "#" not in cluster:
        ret += get_combinations(groups, clusters[1:], cache)
    cache[key] = ret
    return ret


if __name__ == '__main__':
    main()
