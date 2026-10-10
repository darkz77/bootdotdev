def get_letter(book_contents: str) -> dict[str, int]:
    result_dict = {}
    keys = set()
    for word in book_contents.lower():
        keys.add(word)

    for key in keys:
        count = 0
        for letter in book_contents.lower():
            if key == letter:
                count += 1
        result_dict.update({key: count})

    return result_dict

print(get_letter("TttT"))
