from stats import count_words
from stats import character_count
from stats import sorted_character_count
import sys

print("command-line arguments:", sys.argv)
print("Number of arguments:", len(sys.argv))

def get_book_text(path_to_file):   # don't forget colons at the end of function definitions
    with open(path_to_file) as f:
        file_contents = f.read()  # f.read will act on the object called by path. Properly indend lines within with block
    return file_contents

def main ():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]   # Define with relative path
    text = get_book_text(path)   # Call the function with the path
    word_count = count_words(text)
    char_counts = character_count(text)
    sorted_chars = sorted_character_count(char_counts)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['num']}")
    
    print("============= END ===============")
    
main()   # Call the main function