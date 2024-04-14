"""Задание

1) Создать базу данных Cars(через консоль)
2) Добавить 10 машин(pymongo):
● Марка
● Модель
● Пробег
● Стоимость
3) Сделать выборку(написать фильтр-запрос)(pymongo):
● Самая дорогая машина
● Самая дешевая
● Отсортированы по пробегу от меньшего к большему
● Вывести 3 авто с минимальными пробегами

"""


#Создаём базу Cars через PowerShell, добавим 1 объект
# test> use cars_db
# cars_db> db.cars.insertOne({'brand': 'Toyota', 'model': 'CHR', 'mileage': 30000, 'price': 23.5})


#Через PyCharm импортируем модуль pymongo и связываемся с базой данных Cars
import pymongo

client = pymongo.MongoClient('localhost', 27017)
database = client.cars_db
collection = database.cars
db_list = database.list_collection_names()
if "cars" in db_list:
    print("Yes")


#Коллекция данных для залива в БД монго
data = [
    {
        "brand": "BMW",
        "model": "E46",
        "mileage": 314000,
        "price": 6.5
    },
    {
        "brand": "BMW",
        "model": "E60",
        "mileage": 222000,
        "price": 16.3
    },
    {
        "brand": "Ford",
        "model": "Mondeo",
        "mileage": 772000,
        "price": 3.4
    },
    {
        "brand": "VW",
        "model": "Caddy",
        "mileage": 55500,
        "price": 19.3
    },
    {
        "brand": "Opel",
        "model": "Insignia",
        "mileage": 139000,
        "price": 33.6
    },
    {
        "brand": "Suzuki",
        "model": "Vitara",
        "mileage": 89000,
        "price": 31.8
    },
    {
        "brand": "Toyota",
        "model": "Sequoia",
        "mileage": 1268000,
        "price": 20.1
    },
    {
        "brand": "BMW",
        "model": "G01",
        "mileage": 8000,
        "price": 80.5
    },
    {
        "brand": "Ferrari",
        "model": "150",
        "mileage": 111111,
        "price": 111.1
    }
]


"""Разкомментив нижний блок - добавим коллекцию данных в монго"""

# result = collection.insert_many(data)
# print(f"id: {result.inserted_ids}")

"""Заккоментим верхний блок, чтобы снова не добавить данные - далее не трогаем его
Разкомментив нижний блок - проверим добавились ли данные"""

# result = collection.find_one({"brand": "Ferrari"})
# print(result)


#фильтр-запрос "Самая дорогая машина"
def find_most_expensive():
    most_expensive = collection.find().sort({"price": -1})
    for obj in most_expensive:
        print(obj)
        break


find_most_expensive()


#фильтр-запрос "Самая дешевая машина"
def find_most_cheap():
    most_cheap = collection.find().sort("price")
    for obj in most_cheap:
        print(obj)
        break


find_most_cheap()


#фильтр-запрос "Отсортированы по пробегу от меньшего к большему"
def sort_by_mileage():
    sort_mileage = collection.find().sort("mileage")
    for obj in sort_mileage:
        print(obj)


sort_by_mileage()


#фильтр-запрос "Вывести 3 авто с минимальными пробегами"
def sort_by_mileage_3():
    sort_mileage_3 = collection.find().sort("mileage")
    for obj in sort_mileage_3[0:3]:
        print(obj)


sort_by_mileage_3()


