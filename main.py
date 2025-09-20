def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        file_content = f.read()
        return file_content

def count_words(book_content):
    words_list = book_content.split()
    print(f"{len(words_list)} words found in the document")


def main():
    content = get_book_text("books/frankenstein.txt")
    count_words(content)

main()