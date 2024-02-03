def split_list(list: str) -> list[str]:
    new_list = []
    for rec in list:
        new_list.append(rec.split(','))
    return new_list

def strip_array(array: list) -> list:
    for i in range(len(array)):
        if type(array[i]) == str:
            array[i] = array[i].strip()
        else:
            strip_array(array[i])
    return array

def make_dict(clean_list):
    info_list = []
    dict = {}
    for rec in clean_list:
        dict.update({"id": rec[0], "name": rec[1], "age": rec[2]}) # додавання нового словарю з даними кішки
        info_list.append(dict)
    return info_list