

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    words = file_contents.split()
    word_count = len(words)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    letter_result = letter_count(file_contents)
    letter_list = [{'letter': letter, 'count': count} for letter, count in letter_result.items()]
    letter_list.sort(key=lambda x: x['count'], reverse=True)
    for entry in letter_list:
        if entry['letter'].isalpha():
            print(f"The '{entry['letter']}' character was found {entry['count']} times")
    

def letter_count(text):
    letter_count = {}
    for letter in text.lower():
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return(letter_count)

main()