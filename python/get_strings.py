def get_strings(city):
    city = city.lower().replace(" ", "")
    ans = [""] * 26
    order = ""
    for i in city:
        if i not in order:
            order += i
    for i in city:
        ans[ord(i) - 97] += "*"
    return ",".join([i + ":" + ans[ord(i) - 97] for i in order])

print(get_strings("Chicago"))