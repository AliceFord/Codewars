# A program to change some words into Simple Pig Latin


def pig_it(text):
    text = text.split(" ")

    for i in range(len(text)):
        if text[i] == "!" or text[i] == "?":
            pass
        else:
            temp = text[i][:1]
            ans = text[i][1:]
            ans += temp
            ans += "ay"
            text[i] = ans

    text = ' '.join(text)

    return text


print(pig_it("Pig latin is cool"))
