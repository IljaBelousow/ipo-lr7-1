#создаем список с названием books
books = [
    {
       "title": "Феи Винск",
        "author": "Радуга.продакшен",
        "year": "2011",
    },
    {
       "title": "Май литл пони",
        "author": "Лорен Фауст",
        "year": "2022",
    },
    {
       "title": "Спанч Боб",
        "author": "Стивен Хиллинбёрг",
        "year": "1999",
    },
    {
       "title": "Друзья ангелов",
        "author": "Симона Ферри",
        "year": "2007",
    },
    {
       "title": "Мимимишки",
        "author": "Паравоз",
        "year": "2015",
    }
]
for i in books:
    print("---------------------- Книга", i + 1, "-----------------------")
    print("Название:", i["title"], ", Автор:", i["author"])
    print("-----------------------", i["year"], "-------------------------")
    print("")  