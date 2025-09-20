def count_words(book_content):
    words_list = book_content.split()
    print(f"Found {len(words_list)} total words")

def count_characters(book_content):
    character_dict = {}
    for char in book_content.lower():
        if char in character_dict:
            character_dict[char] += 1
        else:
            character_dict[char] = 1
    return character_dict

def sort(unsorted_dict):
    new_dict = []
    for key, value in unsorted_dict.items():
        new_dict.append({"char": key, "num": value})
    new_dict.sort(reverse=True, key=sort_by)
    return new_dict

def sort_by(items):
    return items["num"]
