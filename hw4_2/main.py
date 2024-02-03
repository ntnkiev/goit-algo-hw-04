from data import load_data
from make_dict import split_list, strip_array, make_dict

def get_cats_info(filename: str) -> list:
    raw_data = load_data(filename) #читання файлу
    splitted_data = split_list(raw_data) #розбиття строки по комах
    stripped_data = strip_array(splitted_data) #очищення всіх елементівсписку від пробільних символів
    return make_dict(stripped_data)

def main():
    cats_info = get_cats_info("hw4_2\\cats_file.txt")
    print(cats_info)

if __name__ == "__main__":
    main()