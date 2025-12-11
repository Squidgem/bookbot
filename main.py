from stats import get_word_count
from stats import get_char_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    words = get_word_count(text)
    print(f"Found {words} total words")
    char_counts = get_char_count(text)
    print(char_counts)
    
def get_book_contents(path):
    with open(path) as f:
        return f.read()

main()