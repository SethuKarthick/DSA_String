def is_valid_ip(string):
    ip_address_found = []

    for i in range(1, min(len(string), 4)):
        current_ip_address_parts = ["", "", "", ""]


        current_ip_address_parts[0] = string[:i]
        if not is_valid_part(current_ip_address_parts[0]):
            continue

        for j in range(i+1, i+min(len(string)-i, 4)):
            current_ip_address_parts[1] = string[i:j]
            if not is_valid_part(current_ip_address_parts[1]):
                continue
                
            for k in range(j+1,  j+min(len(string)-j, 4)):
                current_ip_address_parts[2]  = string[j:k]
                current_ip_address_parts[3] = string[k:]

                if is_valid_part(current_ip_address_parts[2]) and is_valid_part(current_ip_address_parts[3]):
                    ip_address_found.append('.'.join(current_ip_address_parts))
    return ip_address_found

def is_valid_part(string):
    string_to_int = int(string)
    if string_to_int > 255:
        return False
    return len(string) == len(str(string_to_int))


Ip = is_valid_ip(string='1921680')
print(Ip)