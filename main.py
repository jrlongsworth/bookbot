def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    word_count = get_word_count(text)
    chars_dict = get_letter_counts(text)
    chars = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, word_count, chars)

def get_book(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def sort_on(dictionary):
    return dictionary["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def get_letter_counts(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered >= 'a' and lowered <= 'z':
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered]  = 1
    return chars

def print_report(book_path, word_count, chars):
    print(f"--- Being report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for char in chars:
        print(f"The '{char["char"]}' character was found {char["num"]} times")
    print("--- End Report ---")

main()