def main():
    book_path = "books/frankenstein.txt"
    text = get_book_contents(book_path)
    print(text)

def get_book_contents(path):
    with open(path) as f:
        return f.read()
    
main()