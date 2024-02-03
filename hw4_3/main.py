from colorama import *
from pathlib import Path

init(autoreset=True)

# print(Style.BRIGHT + "Hello world!" + Style.RESET_ALL)
# print(Fore.GREEN + "Hello world!")
# print(Back.RED + "Hello world!")
# print(Fore.GREEN + "Hello world!")

# Створення об'єкту Path для директорії
directory = Path("C:\\Python_Test")
level = 0

def print_tree(directory):
    global level
    current = []
    for path in directory.iterdir():
        # print(path)
        print("\u2523" if path.is_dir() else "\u2503", "\u2501"*level*4 if path.is_dir() else " "*level*4, Fore.RED + "Folder: " if path.is_dir() else Fore.GREEN + "File: ", path.name)
        if path.is_dir():
            level += 1
            print("\u2503", " " * level * 4, end = '')
            print_tree(path)
            level -= 1
    return None

def main():
    print(Fore.YELLOW + "\u2752", Fore.YELLOW + directory.name)
    print_tree(directory)

if __name__ == "__main__":
    main()