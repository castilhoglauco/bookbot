from stats import count_words, count_characters, sort
import sys

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        file_content = f.read()
        return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    content = get_book_text(sys.argv[1])

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    count_words(content)
    print("----------- Character Count ----------")
    sorted_content = sort(count_characters(content))
    for item in sorted_content:
        if item["char"].isalpha():
          print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")


main()