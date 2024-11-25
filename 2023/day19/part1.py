def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = [line.rstrip('\n') for line in file.readlines()]
    workflows = {}
    ratings = []
    i = 0
    while lines[i] != '':
        key = lines[i].split('{')[0]
        values = lines[i].split('{')[1][:-1].split(',')
        workflows[key] = values
        i += 1
    i += 1
    while i < len(lines):
        ratings.append([int(x[2:]) for x in lines[i][1:-1].split(',')])
        i += 1

    sum_accepted = 0
    for rating in ratings:
        workflow = 'in'
        while workflow not in ['A', 'R']:
            workflow = get_target(workflows[workflow], rating)
        if workflow == 'A':
            sum_accepted += sum(rating)
    print('sum accepted ratings: ' + str(sum_accepted))


def get_target(workflow, rating):
    for condition in workflow:
        if '<' in condition:
            cmp = int(condition.split('<')[1].split(':')[0])
            target = condition.split('<')[1].split(':')[1]
            match condition.split('<')[0]:
                case 'x':
                    if rating[0] < cmp:
                        return target
                case 'm':
                    if rating[1] < cmp:
                        return target
                case 'a':
                    if rating[2] < cmp:
                        return target
                case 's':
                    if rating[3] < cmp:
                        return target
        else:
            if '>' in condition:
                cmp = int(condition.split('>')[1].split(':')[0])
                target = condition.split('>')[1].split(':')[1]
                match condition.split('>')[0]:
                    case 'x':
                        if rating[0] > cmp:
                            return target
                    case 'm':
                        if rating[1] > cmp:
                            return target
                    case 'a':
                        if rating[2] > cmp:
                            return target
                    case 's':
                        if rating[3] > cmp:
                            return target
            else:
                return condition


if __name__ == '__main__':
    main()
