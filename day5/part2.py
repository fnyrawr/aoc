import concurrent.futures
import sys


def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    # read file
    # get seed numbers from ranges
    seeds = list(map(int, lines[0].split(':')[1].strip().split(' ')))
    i = 3
    j = 0
    soil_map = {}
    while lines[i] != '\n':
        line = list(map(int, lines[i].strip().split(' ')))
        # SourceFrom = [Range, Destination]
        soil_map[j] = {'start': line[1], 'end': line[1] + line[2], 'dest': line[0]}
        i += 1
        j += 1

    i += 2
    j = 0
    fertilizer_map = {}
    while lines[i] != '\n':
        line = list(map(int, lines[i].strip().split(' ')))
        fertilizer_map[j] = {'start': line[1], 'end': line[1] + line[2], 'dest': line[0]}
        i += 1
        j += 1

    i += 2
    j = 0
    water_map = {}
    while lines[i] != '\n':
        line = list(map(int, lines[i].strip().split(' ')))
        water_map[j] = {'start': line[1], 'end': line[1] + line[2], 'dest': line[0]}
        i += 1
        j += 1

    i += 2
    j = 0
    light_map = {}
    while lines[i] != '\n':
        line = list(map(int, lines[i].strip().split(' ')))
        light_map[j] = {'start': line[1], 'end': line[1] + line[2], 'dest': line[0]}
        i += 1
        j += 1

    i += 2
    j = 0
    temperature_map = {}
    while lines[i] != '\n':
        line = list(map(int, lines[i].strip().split(' ')))
        temperature_map[j] = {'start': line[1], 'end': line[1] + line[2], 'dest': line[0]}
        i += 1
        j += 1

    i += 2
    j = 0
    humidity_map = {}
    while lines[i] != '\n':
        line = list(map(int, lines[i].strip().split(' ')))
        humidity_map[j] = {'start': line[1], 'end': line[1] + line[2], 'dest': line[0]}
        i += 1
        j += 1

    i += 2
    j = 0
    location_map = {}
    while i < len(lines):
        line = list(map(int, lines[i].strip().split(' ')))
        location_map[j] = {'start': line[1], 'end': line[1] + line[2], 'dest': line[0]}
        i += 1
        j += 1

    maps = {'soil': soil_map, 'fertilizer': fertilizer_map, 'water': water_map, 'light': light_map,
            'temperature': temperature_map, 'humidity': humidity_map, 'location': location_map}

    # map seeds to location
    best_location = sys.maxsize
    for i in range(int(len(seeds)/2)):
        start_range = seeds[i*2]
        end_range = start_range + seeds[i*2+1]
        iterations = end_range-start_range
        print('searching best location in range {} to {} ({} iterations)'.format(start_range, end_range, iterations))
        with concurrent.futures.ThreadPoolExecutor() as executor:
            for seed in range(start_range, end_range):
                future = executor.submit(get_location, seed=seed, maps=maps)
                best_location = min(best_location, future.result())

    print('Best location: ' + str(best_location))


def get_location(seed, maps):
    # map soil
    soil = get_mapping(seed, maps['soil'])
    # map fertilizer
    fertilizer = get_mapping(soil, maps['fertilizer'])
    # map water
    water = get_mapping(fertilizer, maps['water'])
    # map light
    light = get_mapping(water, maps['light'])
    # map temperature
    temperature = get_mapping(light, maps['temperature'])
    # map humidity
    humidity = get_mapping(temperature, maps['humidity'])
    # map location
    return get_mapping(humidity, maps['location'])


def get_mapping(seed, map_pattern):
    for pattern in map_pattern:
        if (seed >= map_pattern[pattern]['start']) and (seed < map_pattern[pattern]['end']):
            return (seed - map_pattern[pattern]['start']) + map_pattern[pattern]['dest']
    return seed


if __name__ == '__main__':
    main()