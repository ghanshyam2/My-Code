import collections


# input = aaaabbbccz
# output = 4a3b2c1z

def count_char(str_ch):
    prev = str_ch[0]
    output = ''
    count = 1
    i = 1
    while i < len(str_ch):
        if str_ch[i] == prev:
            count += 1
        else:
            output += str(count)+prev
            prev = str_ch[i]
            count = 1
        if i == len(str_ch) - 1:
            output += str(count)+prev
        i += 1
    # count = collections.Counter(str_ch)
    # output = ""
    # for key, val in count.items():
    #     output += str(val) + key

    return output


print(count_char("aaaabbbccz"))
print(count_char("aaaaabbbbcccxxz"))
