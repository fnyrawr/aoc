import re


def main():
    lines = [x for x in open('input.txt').read().strip().split('\n\n')]
    workflows, ratings = lines

    ratings = [ints(x) for x in ratings.split("\n")]
    workflows = {x.split("{")[0]: x.split("{")[1][:-1] for x in workflows.split("\n")}

    combinations = 0
    for rng in acceptance_ranges_outer(workflows, 'in'):
        val = 1
        for low, high in rng:
            val *= high - low + 1
        combinations += val
    print('Combinations: ' + str(combinations))


def ints(s):
    return list(map(int, re.findall(r'\d+', s)))


def evaluate(rating, workflows, workflow):
    conditions = workflows[workflow]
    x, m, a, s = rating
    for it in conditions.split(","):
        if it == "R":
            return False
        if it == "A":
            return True
        if ":" not in it:
            return evaluate(rating, workflows, it)
        cond = it.split(":")[0]
        if eval(cond):
            if it.split(":")[1] == "R":
                return False
            if it.split(":")[1] == "A":
                return True
            return evaluate(rating, workflows, it.split(":")[1])
    raise Exception(conditions)


def both(ch, gt, val, ranges):
    ch = 'xmas'.index(ch)
    ranges2 = []
    for rng in ranges:
        rng = list(rng)
        low, high = rng[ch]
        if gt:
            low = max(low, val + 1)
        else:
            high = min(high, val - 1)
        if low > high:
            continue
        rng[ch] = (low, high)
        ranges2.append(tuple(rng))
    return ranges2


def acceptance_ranges_outer(workflows, work):
    return acceptance_ranges_inner(workflows, workflows[work].split(","))


def acceptance_ranges_inner(workflows, w):
    it = w[0]
    if it == "R":
        return []
    if it == "A":
        return [((1, 4000), (1, 4000), (1, 4000), (1, 4000))]
    if ":" not in it:
        return acceptance_ranges_outer(workflows, it)
    cond = it.split(":")[0]
    gt = ">" in cond
    ch = cond[0]
    val = int(cond[2:])
    val_inverted = val + 1 if gt else val - 1
    if_cond_is_true = both(ch, gt, val, acceptance_ranges_inner(workflows, [it.split(":")[1]]))
    if_cond_is_false = both(ch, not gt, val_inverted, acceptance_ranges_inner(workflows, w[1:]))
    return if_cond_is_true + if_cond_is_false


if __name__ == '__main__':
    main()
