def main():
    textfile = 'test_input.txt.txt'
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

    # get lowest location for seed in range
    seed_found = False
    location = 0
    while not seed_found:
        seed = get_seed(location, maps)
        for i in range(int(len(seeds) / 2)):
            start_range = seeds[i * 2]
            end_range = start_range + seeds[i * 2 + 1]
            if start_range <= seed <= end_range:
                seed_found = True
        if not seed_found:
            location += 1

    print('Best location: ' + str(location))


def get_seed(location, maps):
    # map humidity
    humidity = get_reverse_mapping(location, maps['location'])
    # map temperature
    temperature = get_reverse_mapping(humidity, maps['humidity'])
    # map light
    light = get_reverse_mapping(temperature, maps['temperature'])
    # map water
    water = get_reverse_mapping(light, maps['light'])
    # map fertilizer
    fertilizer = get_reverse_mapping(water, maps['water'])
    # map soil
    soil = get_reverse_mapping(fertilizer, maps['fertilizer'])
    # map seed
    return get_reverse_mapping(soil, maps['soil'])


def get_reverse_mapping(location, map_pattern):
    for pattern in map_pattern:
        if (location >= map_pattern[pattern]['dest'])\
                and (location < map_pattern[pattern]['dest'] + (map_pattern[pattern]['end'] - map_pattern[pattern]['start'])):
            return (location - map_pattern[pattern]['dest']) + map_pattern[pattern]['start']
    return location


if __name__ == '__main__':
    main()