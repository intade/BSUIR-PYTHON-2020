Никаких зависимостей не требуется.
1 лаба: реализована минимальная куча. Идея в том, чтобы заполнить кучу, в которой на вершине всегда находится минимальный элемент, после чего мы соединяем с темповым файлом full в empty, потом снова заполняем кучу. В full лежат результаты прошлых слияний. Результат записывается в sorted.txt

2 лаба: для различных типов данных - различные функции: сначала мы проверяем, являются ли входные данные list'ом, tuple'ом или dict'ом, если нет, то считаем, что это какой-то класс и переводим его в dict. Дальше просто поочередно проверяем на каждый тип и вызываем нужную функцию.
    Из json: получаем токен с помощью функции _get_token и вызываем нужную функцию, возвращающую нужный тип

3 лаба: просто реализован ряд статических методов с помощью декоратора @staticmethod. Также для удобства реализованы __len__, __iter__, __next__ и __getitem__

4 лаба: храним значения прошлых вызовов в коллекции cache, где ключ - аргументы, а значение - результат функции. Если есть значение по ключу, возвращаем его, иначе вызываем функцию

5 лаба: юниттесты с помощью unittest и coverage. Покрытие по каждой лабе около 90 процентов. Единственное по 4 лабе нет юниттестов, потому что там почти нечего проверять

Синглтон : реализован в виде класса, от которого наследуется класс, которому необходим данный паттерн

setup.py : так же реализован
