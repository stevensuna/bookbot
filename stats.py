def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
        letter_count = {}
        for char in text.lower():
            if char not in letter_count:
                letter_count[char] = 0
            letter_count[char] += 1
        return letter_count