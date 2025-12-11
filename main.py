def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    words = get_word_count(text)
    print(f"Found {words} total words")
    
def get_word_count(text):
    word_count = 0 
    for word in text.split():
        word_count += 1
    return word_count
    
def get_book_contents(path):
    with open(path) as f:
        return f.read()

main()