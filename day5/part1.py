def main():
    textfile = 'input.txt'
    with open(textfile, 'r') as file:
        lines = file.readlines()

    # read file
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

    print('seeds:                  ' + str(seeds))
    print('seed 2 soil:            ' + str(soil_map))
    print('soil 2 fertilizer:      ' + str(fertilizer_map))
    print('fertilizer 2 water:     ' + str(water_map))
    print('water 2 light:          ' + str(light_map))
    print('light 2 temperature:    ' + str(temperature_map))
    print('temperature 2 humidity: ' + str(humidity_map))
    print('humidity 2 location:    ' + str(location_map))
    print()

    # map seeds to location
    locations = []
    for seed in seeds:
        # map soil
        soil = get_mapping(seed, soil_map)
        print('seed {:2} -> soil: {:2}'.format(seed, soil))
        # map fertilizer
        fertilizer = get_mapping(soil, fertilizer_map)
        print('soil {:2} -> fertilizer: {:2}'.format(soil, fertilizer))
        # map water
        water = get_mapping(fertilizer, water_map)
        print('fertilizer {:2} -> water: {:2}'.format(fertilizer, water))
        # map light
        light = get_mapping(water, light_map)
        print('water {:2} -> light: {:2}'.format(water, light))
        # map temperature
        temperature = get_mapping(light, temperature_map)
        print('light {:2} -> temperature: {:2}'.format(light, temperature))
        # map humidity
        humidity = get_mapping(temperature, humidity_map)
        print('temperature {:2} -> humidity: {:2}'.format(temperature, humidity))
        # map location
        location = get_mapping(humidity, location_map)
        print('humidity {:2} -> location: {:2}'.format(humidity, location))
        locations.append(location)
        print()
    print('Locations: ' + str(locations))
    print('Best location: ' + str(min(locations)))


def get_mapping(seed, map_pattern):
    for pattern in map_pattern:
        if (seed >= map_pattern[pattern]['start']) and (seed < map_pattern[pattern]['end']):
            return (seed - map_pattern[pattern]['start']) + map_pattern[pattern]['dest']
    return seed


if __name__ == '__main__':
    main()