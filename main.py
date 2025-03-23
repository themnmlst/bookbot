from stats import sort_chars, count_character, get_word_count
import sys

def get_book_test(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents

def main():
    if len(sys.argv) < 2:
        print(f"Usage: python3 main.py <path_to_book>") 
        sys.exit(1)

    file_contents = get_book_test(sys.argv[1])
    word_count = get_word_count(file_contents)
    char_counts = count_character(file_contents)
    sorted_chars = sort_chars(char_counts)
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    print("============= END ===============")

main()