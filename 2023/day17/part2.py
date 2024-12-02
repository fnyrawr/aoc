"""
    reference reddit user leijurv
    https://topaz.github.io/paste/#XQAAAQBUBAAAAAAAAAAzHIoib6py7i/yVWhl9dSCjkM4GPHrtd8B89i1ferannGa/iSPEhSfwXSQjO97mxh41OLgLuTQT5wZp7bL+YFnrXGCd60/JWIJ5WDSmI0hG6+qMtQOj2QXDJktThQfZ6yIaRD6IZd0P7FmvoN12N2kW/FQ0qpK6T1z6dICqSYqO0/Ksi5YYpqJcNN8deanbLf8wUaZ+5epfmFAoDmvOVTVXvFnKco4Us7YFjds3fPaa954Jf59LhozJtJsgKGwzGe88BZZsMONFj7eorNEm64UlpMkbwm3AX/f5q4PRVDYidntpWQAOacIkW6P5qxfeTyoBlErtzaTP5jf8rGuQiZfpmE5Y+4Rnyq0tOA0sjBsg5VtPNZsYnWssqb1QXz/C9k+GpgJWC7wibMKcO6LzbFeP3L9zi6gzg1cbzGnh0VMsBaat3ydPU977qz/+phzmMAn4TORuFsJneXjbnokMULP7VkIyB3iY9wyPR3Fq8G09fvU/abyU9ZXNGFZvdfeH1RXmRxd638aQUjWEzugbC7VD4vM/iJEkhhJddEKWgl3642Z0Lgb/RrESf8sAicMP7ehT4u8TNRq4ZKPJJp7DvevdrsSJJ8vM+GuqPD+dqa5/Ee3qsJYdjyCm5j1CpYrJSL+KBjeUWho+l5mablrGuP6/R3+dfiEOfJY0p8nxp+l2C3T+nwpw5s3hgOKXYLdTb+HaMceyd+EAz4R32xkCurWxa5x18ym7USc/CFfmlk5M1WTmgYgShgeG39+cMf/gaRH1A==
"""

from heapq import heappop, heappush


def main():
    textfile = 'input.txt'
    lines = [[int(y) for y in x] for x in open(textfile).read().strip().split('\n')]
    heat_loss = find_path_min_heat_loss(lines)
    print('Optimal path incurs a heat loss of ' + str(heat_loss))


def find_path_min_heat_loss(lines):
    # heat_loss, x, y, disallowedDirection
    min_distance = 4
    max_distance = 10
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    q = [(0, 0, 0, -1)]
    visited = set()
    heat_losses = {}
    while q:
        heat_loss, x, y, dd = heappop(q)
        if x == len(lines) - 1 and y == len(lines[0]) - 1:  # goal x, goal y
            return heat_loss
        if (x, y, dd) in visited:
            continue
        visited.add((x, y, dd))
        for direction in range(4):
            curr_heat_loss = 0
            if direction == dd or (direction + 2) % 4 == dd:
                # can't go this way
                continue
            for distance in range(1, max_distance + 1):
                xx = x + directions[direction][0] * distance
                yy = y + directions[direction][1] * distance
                if inr((xx, yy), lines):
                    curr_heat_loss += lines[xx][yy]
                    if distance < min_distance:
                        continue
                    nc = heat_loss + curr_heat_loss
                    if heat_losses.get((xx, yy, direction), 1e100) <= nc:
                        continue
                    heat_losses[(xx, yy, direction)] = nc
                    heappush(q, (nc, xx, yy, direction))


def inr(pos, arr):
    return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))


if __name__ == '__main__':
    main()
