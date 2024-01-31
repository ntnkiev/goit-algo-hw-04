def load_data(filename: str) -> list[str]:
    try:
        with open(filename, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        print('File not found')
        exit()

def clean_data(salaries_list: list[str]) -> list[float]:
    clean_list = []
    for sol in salaries_list:
        clean_list.append(float(sol.split(',')[1].strip()))
    return clean_list