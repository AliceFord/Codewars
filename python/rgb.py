def rgb(r, g, b):
    r = greaterLessRGB(r)
    g = greaterLessRGB(g)
    b = greaterLessRGB(b)
    return (("0" + (hex(r)[2:]))[len(hex(r)[2:])-1:] + ("0" + (hex(g)[2:]))[len(hex(g)[2:])-1:] + ("0" + (hex(b)[2:]))[len(hex(b)[2:])-1:]).upper()


def greaterLessRGB(x):
    if x > 255: x = 255
    if x < 0: x = 0
    return x


print(rgb(255, 2555, 255))
