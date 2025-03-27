from stats import count_words, count_letters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text('./books/frankenstein.txt')
    num_words = count_words(book_text)
    num_letters = count_letters(book_text)
    print(f"{num_words} words found in the document")
    print(f"{num_letters} letters found in the document")

main()