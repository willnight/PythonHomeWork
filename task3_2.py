fields = dict(name='Имя', surname='Фамилия', birth_year='Год рождения', city='Город проживания', email='Email',
              phone='Телефон')


def get_user_info(**kwargs):
    """Вывод информации о пользователе в строку

    kwargs:
        информация о пользователе с параметрами
    return:
        строка с данными о пользователе
    """
    user_info = list()
    for k, v in kwargs.items():
        user_info.append(f"{fields.get(k)}: {v}")
    return ", ".join(user_info)


print(get_user_info(name='Анастасия', surname='Романова', birth_year='2002',
                    city='Москва', email='testmail@gmail.com', phone='+79113325468'))
