"""
    reference reddit user 4HbQ
    https://topaz.github.io/paste/#XQAAAQCWAQAAAAAAAAA4GwhH7u5OdXNRlPeIKYn01V1xhpyceJIwtT5HvB9jA7zH7F67Rry3WbFjXXlg+rj3O3Pcr0jV1/vTXP/7jdZNkrMTQPkbSnuvlXFjzrTfvX3Ir+VxA2REBE39YUc3u64mdAog36DTi6Cd3mk6MAP8HSDqMVD0qJWDIkT/T1frVVjq6Vwl5B9bhr/EfMYhQ76SVYOJ6B7nLXSvqLGiHL5rPpGvcRdh0YoH1xiJatTkING88zdpuFObWwPvuD4cTrcfh/S8kGfa8HfqLQ2orimQG0QsuKI0HONFCDJETbWr//xp3YC3FDnfyWQt6ckdQnNJ6Oha4P/4frRL
"""


def main():
    textfile = 'input.txt'
    dig_plan = list(map(str.split, open(textfile)))
    directions = {'0': (1, 0), '1': (0, 1), '2': (-1, 0), '3': (0, -1)}
    tiles = f((directions[c[7]], int(c[2:7], 16)) for _, _, c in dig_plan)
    print('tiles: ' + str(tiles))


def f(steps, pos=0, ans=1):
    for (x, y), n in steps:
        pos += x * n
        ans += y * n * pos + n / 2
    return int(ans)


if __name__ == '__main__':
    main()