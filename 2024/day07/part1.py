from collections import deque

EQUATIONS = (
    lambda x,y: x+y,
    lambda x,y: x*y,
)

def test_equations(val: int, eq: deque):
    functions = EQUATIONS
    res = eq.popleft()
    queue = {res}
    while eq:
        next_val = eq.popleft()
        new_queue = set()
        for r in queue:
            if r > val:
                continue
            for func in functions:
                new_queue.add(func(r, next_val))
        queue = new_queue
    return val in queue

def main():
    data = []
    with open('input.txt') as file:
        lines = file.readlines()
    for line in lines:
            key, val = line.strip().split(":")
            data.append((int(key), deque([int(x.strip()) for x in val.split(" ") if x])))
    calibration_result = sum(key for key, value in data if test_equations(key, value))
    print(calibration_result)

if __name__ == "__main__":
    main()