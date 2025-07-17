def reduce(name):
    # convert name into compatible format
    output = ""
    for c in name:
        if c.isalpha() or c.isnumeric():
            output += c.lower()
        elif (c == ' ' or c == '-') and output[-1] != '_':
            output += '_'
        elif c == 'é':
            output += 'e'
    return output