def get_num_words(text):
    """Splits the text into a list and counts the number of items in that list."""
    words = text.split()
    return len(words)