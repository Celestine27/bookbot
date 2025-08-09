def bot_art(book_p, num_w, book_l):
    """Generates book bot art"""
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_p}")
    print("----------- Word Count ----------")
    print(f"Found {num_w} total words")
    print("--------- Character Count -------")
    for item in book_l:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

