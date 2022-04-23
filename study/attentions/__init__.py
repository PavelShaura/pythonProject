attention = {"out": "Вы вышли из системы", "noaccess": "У вас нет доступа в этот раздел",
             "unknown": "Неизвестная ошибка", "timeout": "Система долго не отвечает",
             "robot": "Ваши действия похожи на робота"}


def get_errors(*error):
    result = []

    for i in error:
        result.append(attention.get(i, "Такой ошибки нет"))
    return result


print(get_errors("noaccess", "out", ""))
