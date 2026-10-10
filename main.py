from stats import get_num_words, get_letter


def get_book_text(path: str) -> str:
    with open(path) as f:
        book_contents = f.read()
    return book_contents


def main() -> None:
    path = "./books/frankenstein.txt"
    book_content = get_book_text(path)
    num_words = get_num_words(book_content)
    print(f"Found {num_words} total words")

    dict_letters = get_letter(book_content)
    print(dict_letters)


if __name__ == "__main__":
    main()
