from stats import get_word_count
from stats import get_char_count
from stats import print_report
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_contents(book_path)
    words = get_word_count(text)
    print(f"Found {words} total words")
    char_counts = get_char_count(text)
    report = print_report(char_counts)
    print(report)
    
def get_book_contents(path):
    with open(path) as f:
        return f.read()

main()