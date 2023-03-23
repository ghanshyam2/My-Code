def char_count(str_char):
    prev = str_char[0]
    output = ''
    counts = 1
    ini = 1
    while ini < len(str_char):
        if str_char[ini] == prev:
            counts += 1
        else:
            output += prev + str(counts)
            prev = str_char[ini]
            counts = 1
        if ini == len(str_char) - 1:
            output += prev + str(counts)
        ini += 1

    return output


print(char_count("aaaabbbcccdz"))
