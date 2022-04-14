def underscorify_substring(string, substring):

    locations = get_substring_location(string, substring)
    collated_locations = collate_locations(locations)
    return underscorify(string, collated_locations)


def get_substring_location(string, substring):
    start_idx = 0
    locations = []

    while start_idx < len(string):
        next_idx = string.find(substring, start_idx)
        if next_idx != -1:
            locations.append([next_idx, next_idx+len(substring)])
            start_idx = next_idx+1
        else:
            break

    return locations

def collate_locations(locations):
    new_locations = [locations[0]]
    previous = new_locations[0]

    for i in range(1, len(locations)):
        current = locations[i]

        if current[0] <= previous[1]:
            previous[1] = current[1]
        else:
            new_locations.append(current)
            previous = current

    return new_locations

def underscorify(string, locations):
    location_idx = 0
    string_idx = 0
    final_char = []
    in_between_underscores = False
    i = 0

    while string_idx < len(string) and location_idx < len(locations):
        if string_idx == locations[location_idx][i]:
            final_char.append('_')
            in_between_underscores = not in_between_underscores
            if not in_between_underscores:
                location_idx += 1
            i = 0 if i == 1 else 1
        final_char.append(string[string_idx])
        string_idx += 1

    if location_idx < len(locations):
        final_char.append('_')
    elif string_idx < len(string):
        final_char.append(string[string_idx:])

    return ''.join(final_char)



underscored_string = underscorify_substring(string = 'testthis is testtest to see if testtesttest it works', substring='test')
print(underscored_string)




