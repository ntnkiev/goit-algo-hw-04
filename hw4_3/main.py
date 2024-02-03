from colorama import *
from pathlib import Path

init(autoreset=False)

# print(Style.BRIGHT + "!!!" + Style.RESET_ALL)
# print(Fore.GREEN + "!!!")
# print(Back.RED + "!!!")
# print(Fore.GREEN + "!!!")

# Створення об'єкту Path для директорії
directory = Path("C:\SynologyDrive\Work\Python_test")
level = 0

def print_tree(directory):
    global level
    current = []
    try:
        for path in directory.iterdir():
            # print(path)
            print(("\u2523" if path.is_dir() else "\u2503") + ("\u2501"*level*4 if path.is_dir() else " "*level*4) + Fore.GREEN + "Folder: " if path.is_dir() else Fore.BLUE + "File: ", path.name + Style.RESET_ALL)
            if path.is_dir():
                level += 1
                # print("\u2503", " " * level * 4, end = '')
                print_tree(path)
                level -= 1
        return None
    except PermissionError:
        print(Fore.RED + path + "Permission Denied")
    except FileNotFoundError:
        print(Fore.RED + "Error: Directory not found")

def main():
    print(Fore.YELLOW + "\u2752", Fore.YELLOW + directory.name + Style.RESET_ALL)
    print_tree(directory)

if __name__ == "__main__":
    main()