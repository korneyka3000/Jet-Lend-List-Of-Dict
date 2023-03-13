'''Дано: список dict-объектов вида вида {"key": "value"},
 например
 [{"key1": "value1"},
  {"k1": "v1", "k2": "v2", "k3": "v3"},
   {},
    {},
     {"key1": "value1"},
      {"key1": "value1"},
       {"key2": "value2"}].

Напишите функцию, которая удаляет дубликаты из этого списка.
 Для примера выше возвращаемое значение может быть равно
  [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {"key2": "value2"}].
Обязательное условие: функция не должна иметь сложность O(n^2).'''


def remove_duplicates(lst: list) -> list:
    return list({str(x): x for x in lst})

lst = [{"key1": "value1"},
       {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
new_lst = remove_duplicates(lst)
print(new_lst)
