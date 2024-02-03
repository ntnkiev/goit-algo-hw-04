def load_data(filename: str) -> list[str]: #читання файлу
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print('File not found')
        exit()