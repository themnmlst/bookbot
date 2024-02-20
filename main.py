def main():
    import collections

    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        words = file_contents.split()

    dict_of_characters = collections.defaultdict(int)

    word_count = 1

    def characters(stream):
        lowered_stream = stream.lower()
        for char in lowered_stream:
            if char in [" ", "\n"]:
                nonlocal word_count
                word_count += 1
            if char.isalpha():
                dict_of_characters[char] += 1

    characters(file_contents)

    list_of_dict_of_characters = []

    for char, occurrence in dict_of_characters.items():  # Use items() to get key-value pairs
        newDict = {
            "char": char, "occurrence": occurrence  # Corrected the key name
            }

        list_of_dict_of_characters.append(newDict)

    def sort_on(dict):
        return dict["occurrence"]

    list_of_dict_of_characters.sort(reverse=True, key=sort_on)  # Pass the function to key parameter

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for item in list_of_dict_of_characters:
        print(f"The {item['char']} character was found {item['occurrence']} times")


main()

