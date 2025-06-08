"""
File: DictionaryCount.py
Author: Vishal Singh.
"""
def main():
    # Importing words from a file name words.
    words = load_words_from_file("words.txt")
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    print(word_counts)


def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)

    return words

if __name__ == '__main__':
    main()
