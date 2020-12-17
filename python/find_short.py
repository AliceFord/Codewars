def find_short(s):
    l = 10000000
    for item in s.split(" "):
        if len(item) < l: l = len(item)
    return l

print(find_short("bitcoin take over the world maybe who knows perhaps"))