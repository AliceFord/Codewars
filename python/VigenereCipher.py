class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        output = ""
        for i in text:
            if i in self.alphabet:
                temp = ord(i) + self.key[i % len(self.key)]
                temp -= len(self.key) // (len(temp) % 26 + 96)
                output += temp
            else:
                output += i
        return output

    def decode(self, text):
        pass


c = VigenereCipher("password", "abcdefghijklmnopqrstuvwxyz")

print(c.encode("codewars"))