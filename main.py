
def main():
    directory = "books/frankenstein.txt"
    with open(directory) as book:
        read_book = book.read()

        c_word = count_word(read_book)
        c_char = count_char(read_book)
        c_dict = sort_dict(c_char)

        title = directory.split('.')[0].split('/')[1].upper()
        report(title, c_dict, c_word)

def count_word(book):
    word_count = len(book.split())
    return word_count

def count_char(book):
    char_dictionary = {}
    for char in book:
        c = char.lower()
        if c in char_dictionary:
            char_dictionary[c] += 1
        else:
            char_dictionary[c] = 1
    return char_dictionary

def sort_dict(dictionary):
    sort = dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
    keys = list(sort.keys())
    sorted_dict = []
    for key in keys:
        if key.isalpha():
            sorted_dict.append([key, sort[key]])
    return sorted_dict

def report(title, char_count, word_count):
    print(f'--- Begin report of {title} ---')
    print(f'{word_count} words found in the document')
    for [char, count] in char_count:
        print(f'The {char} character was found {count} times')
    print('--- End report ---')

main()