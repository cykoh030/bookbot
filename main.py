from string import ascii_lowercase


def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_book_word_count(path):
    with open(path) as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        return word_count

def get_book_character_count(path):
    with open(path) as f:
        file_contents = f.read().lower()
        letter_counts = {}
        for letter in ascii_lowercase:
            letter_counts[letter] = file_contents.count(letter)
        return letter_counts

def main():
    book_path = "books/frankenstein.txt"
    book_word_count = get_book_word_count((book_path))
    letter_counts = get_book_character_count(book_path)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{book_word_count} words found in the document\n")
    for letter in letter_counts:
        print(f"The '{letter}' character was found {letter_counts[letter]} times")
    print("--- End report ---")

main()