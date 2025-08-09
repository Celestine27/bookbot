def get_num_words(text):
    """Splits the text into a list and counts the number of items in that list."""
    words = text.split()
    return len(words)

def get_num_char(text):
    """Loops through a list and adds characters from the text to a dictionary."""
    char_value = {}
    for c in text.lower():
        if c not in char_value:
            char_value[c] = 1
        else:
            char_value[c] += 1
    return char_value

def sort_on(items):
       """Sorts items based on highest value to lowest."""
       return items["num"]

def book_bot(num):
    """Makes a dictionary of char and num and puts them into a list."""
    book_list = []
    for c, n in num.items():
        book_dict = {}
        book_dict["char"] = c
        book_dict["num"] = n
        book_list.append(book_dict)
    
    book_list.sort(reverse=True, key=sort_on)
    return book_list
     

        
        

    



