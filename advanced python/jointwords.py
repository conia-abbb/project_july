from functools import reduce
def join_strings(words):
    black = ""
    for word in words:
        black += word + " "
    return black
words = ["i", "came","i", "saw", "i", "conquered"]
total = reduce(lambda item, running_total: item + " " + running_total , words)
print(total)
icameisawiconquered = join_strings(words)
print(join_strings(words))