from data import load_data
from make_dict import make_dict

def get_cats_info(filename: str) -> list:
    raw_data = load_data(filename) # читання файлу
    return make_dict(raw_data) # 

def main():
    cats_info = get_cats_info("hw4_2\\cats_file.txt")
    print(cats_info)

if __name__ == "__main__":
    main()