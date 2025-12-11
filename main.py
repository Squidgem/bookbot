from stats import get_word_count

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    words = get_word_count(text)
    print(f"Found {words} total words")
    
def get_book_contents(path):
    with open(path) as f:
        return f.read()

main()