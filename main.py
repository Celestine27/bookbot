from stats import get_num_words, get_num_char, book_bot
from art import bot_art


def main():
    book_path = "./books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_char = get_num_char(text)
    book_list = book_bot(num_char)
    print(bot_art(book_path, num_words, book_list))
    


def get_book_text(path):
    """Reads a text file and returns it's content as a string."""
    with open(path) as f:
        return f.read()
        
    
main()












