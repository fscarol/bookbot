from stats import get_num_words, char_appearances, sort_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        text = get_book_text(sys.argv[1])
        num_words = get_num_words(text)
        words_dict = char_appearances(text)
        sorted_dict = sort_dict(words_dict)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        print(sorted_dict)
        print("============= END ===============")

#entry point
main()