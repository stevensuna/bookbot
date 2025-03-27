from stats import count_letters, count_words, sort_letter_counts
# This script reads a text file and counts the number of words and letters in it.
# It uses the functions count_words and count_letters from the stats module.
# The file is expected to be in the same directory as this script.
# The file name is 'frankenstein.txt' and it is located in the 'books' subdirectory.
# The script prints the number of words and letters found in the document.
# The script is designed to be run from the command line.
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
# The script uses the sys module to read command line arguments.

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    num_letters = count_letters(book_text)
    sorted_chars = sort_letter_counts(num_letters)
    print("\n============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_info in sorted_chars:
        if char_info['char'].isalpha():
            print(f"{char_info['char']}: {char_info['count']}")
main()