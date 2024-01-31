def make_dict(list) -> list:
    dict = {}
    dict_item = []
    info_list = []
    for rec in list:
        dict_item.append(rec.split(',')) # розділ по комах
    for rec in dict_item: # вилучення пробільних символів всіх елементів
        for i in range(len(rec)):
            rec[i] = rec[i].strip()
    for rec in dict_item:
        dict.update({"id": rec[0], "name": rec[1], "age": rec[2]}) # додавання нового словарю з даними кішки
        info_list.append(dict)
    return info_list