def get_word_count(text):
    word_count = 0 
    for word in text.split():
        word_count += 1
    return word_count
