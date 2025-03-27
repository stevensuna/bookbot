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

def sort_letter_counts(letter_counts):
    # Convert dictionary to list of dictionaries with char and count keys
    char_list = [{'char': char, 'count': count} for char, count in letter_counts.items()]
    # Sort list by count in descending order
    sorted_chars = sorted(char_list, key=lambda x: x['count'], reverse=True)
    return sorted_chars
