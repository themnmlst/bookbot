def get_word_count(file_contents):
    words = file_contents.split()
    return len(words)  # Return instead of print

def count_character(file_contents):
    result = {}
    for character in file_contents:
        if character.lower() not in result:
            result[character.lower()] = 1
        else:
            result[character.lower()] += 1
    return result

def sort_chars(char_dict):
    chars_list = []
    
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    
    def sort_on(dict):
        return dict["count"]
    
    chars_list.sort(reverse=True, key=sort_on)
    
    return chars_list