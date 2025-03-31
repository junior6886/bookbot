from stats import get_num_words, get_num_occurrances
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents
    
def report(file_path):
    text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    get_num_words(text)
    print("--------- Character Count -------")
    dict = get_num_occurrances(text.lower())
    for item in dict:
        print(f"{item}: {dict[item]}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    report(sys.argv[1])
    
main()
