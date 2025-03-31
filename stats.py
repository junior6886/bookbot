def get_num_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")

def get_num_occurrances(text):
    dict = {}
    chars = list(text)
    for c in chars:
        if dict.get(c) == None:
            dict[c] = text.count(c)
    return dict