def main():
    textfile = 'test_input.txt.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()
    hands = []
    # get hand values
    for i in range(len(lines)):
        hand = lines[i].split(' ')[0].strip()
        bid = lines[i].split(' ')[1].strip()
        hands.append([hand, get_hand_value(hand), int(bid)])

    # compare them
    hands = qsort(hands)

    # score ranks with bids
    score = 0
    for i in range(len(hands)):
        score += (i+1)*hands[i][2]
        print('Hand: {:5} | Val: {:1} | Rank: {:4} | Bid: {:3} | Jokers: {:1}'.format(hands[i][0], hands[i][1], i+1, hands[i][2], get_joker_count(hands[i][0])))
    print('Score: {}'.format(score))


def qsort(hands):
    if not hands:
        return []
    pivot = hands[0]
    less = [x for x in hands[1:] if compare_hand_ranks(x, pivot) < 1]
    more = [x for x in hands[1:] if compare_hand_ranks(x, pivot) == 1]
    return qsort(less) + [pivot] + qsort(more)


def compare_hand_ranks(hand1, hand2):
    # check pair ranks
    if hand1[1] < hand2[1]:
        return 0
    if hand1[1] > hand2[1]:
        return 1
    # check card ranks
    i = 0
    while i < 6:
        card1 = get_card_value(hand1[0][i])
        card2 = get_card_value(hand2[0][i])
        if card1 < card2:
            return 0
        if card1 > card2:
            return 1
        i += 1
    return -1


def get_hand_value(hand):
    cards = {}
    for i in range(5):
        card = get_card_value(hand[i])
        if card in cards:
            cards[card] += 1
        else:
            cards[card] = 1
    max_same = 1
    second_max_same = 0
    for card in cards:
        if cards[card] >= max_same:
            second_max_same = max_same
            max_same = cards[card]
        else:
            if cards[card] > second_max_same:
                second_max_same = cards[card]
    if max_same == 5:
        return 7  # five of a kind
    if max_same == 4:
        if get_joker_count(hand) == 4:
            return 7  # five of a kind with joker
        if get_joker_count(hand) == 1:
            return 7  # five of a kind with joker
        return 6  # four of a kind
    if max_same == 3:
        if second_max_same == 2:
            if get_joker_count(hand) == 3:
                return 7  # five of a kind with joker
            if get_joker_count(hand) == 2:
                return 7  # five of a kind with joker
            return 5  # full house
        if get_joker_count(hand) == 3:
            return 6  # four of a kind with joker
        if get_joker_count(hand) == 1:
            return 6  # four of a kind with joker
        return 4  # three of a kind
    if max_same == 2:
        if second_max_same == 2:
            if get_joker_count(hand) == 2:
                return 6  # four of a kind with joker
            if get_joker_count(hand) == 1:
                return 5  # full house with joker
            return 3  # two pair
        if get_joker_count(hand) == 2:
            return 4  # three of a kind with joker
        if get_joker_count(hand) == 1:
            return 4  # three of a kind with joker
        return 2  # one pair
    if get_joker_count(hand) == 1:
        return 2  # one pair with joker
    return 1  # high card


def get_joker_count(hand):
    jokers = 0
    for i in range(5):
        if hand[i] == 'J':
            jokers += 1
    return jokers


def get_card_value(char):
    if char in ['2', '3', '4', '5', '6', '7', '8', '9']:
        return int(char)
    if char == 'T':
        return 10
    if char == 'J':
        return 1
    if char == 'Q':
        return 12
    if char == 'K':
        return 13
    if char == 'A':
        return 14
    return 0


if __name__ == '__main__':
    main()