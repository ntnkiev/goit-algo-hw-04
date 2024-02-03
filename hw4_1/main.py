from data import load_data, clean_data
from calculate import calc_average, calc_total

def total_salary(filename: str) -> float:
    raw_data = load_data(filename) #завантаження файлу списка
    salaries_list = clean_data(raw_data) #створення списку зарплат
    return calc_total(salaries_list), calc_average(salaries_list) #повертання результату

def main():
    total, average = total_salary("hw4_1\\salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")

if __name__ == "__main__":
    main()