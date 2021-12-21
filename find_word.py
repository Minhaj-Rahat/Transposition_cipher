import enchant


def find_words(deciphered_text):
    d = enchant.Dict("en_US")
    text = d.suggest(deciphered_text)
    return text
