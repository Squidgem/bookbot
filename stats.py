def get_word_count(text):
    word_count = 0 
    for word in text.split():
        word_count += 1
    return word_count

def get_char_count(text):
    char_count = {}
    lowercase = text.lower()
    for char in lowercase:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count