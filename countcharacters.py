import collections


def char_count_char(string):
    count = collections.Counter(string)
    output = ''
    for key, val in count.items():
        output += key + str(val)
    return output


print(char_count_char("aaabbcccdd"))
