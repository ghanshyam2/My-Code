def replace_char(str_repl):
    # input = a4k3b2
    # output = aeknbd
    global x
    output = ""
    for ch in str_repl:
        if ch.isalpha():
            output += ch
            x = ch
        else:
            dini = int(ch)
            new_ch = chr(ord(x) + dini)
            output += new_ch
    return output


print(replace_char("a4k3b2"))
print(replace_char("a3b2c3d4"))
