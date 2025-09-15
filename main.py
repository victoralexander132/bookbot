import sys
from stats import get_words_count, get_character_count, sort_dictionary


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    words_count = get_words_count(book_text)
    character_count = get_character_count(book_text)
    sorted_dictionary = sort_dictionary(character_count)
    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {filepath}')
    print('----------- Word Count ----------')
    print(f'Found {words_count} total words')
    print('--------- Character Count -------')
    for char_dict in sorted_dictionary:
        if char_dict['character'].isalpha():
            print(f'{char_dict['character']}: {char_dict['num']}')
    print('============= END ===============')


main()