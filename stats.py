def get_num_words(text):
    """Splits the text into a list and counts the number of items in that list."""
    words = text.split()
    return len(words)

def get_num_char(text):
    char_value = {}
    for c in text.lower():
        if c not in char_value:
            char_value[c] = 1
        else:
            char_value[c] += 1
    return char_value

        
        

    



