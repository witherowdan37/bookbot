import sys
from stats import word_count
from stats import char_count
from stats import sorted_list

def get_book_text(path):
    temp = ""
    with open(path) as f:
        temp = f.read()

    return temp

def main():
    if len(sys.argv) <= 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    num = 0
    text = ""
    txt_stats = {}
    dict_list = []

    #path = "books/frankenstein.txt"
    path = sys.argv[1]
    
    text = get_book_text(path)
    num = word_count(text)  
    txt_stats = char_count(text)
    dict_list = sorted_list(txt_stats)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num} total words")
    print("--------- Character Count -------")
  #  for i in range(0, len(dict_list)):
    for item in dict_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
main()