# DiscraProject
Функция rsa() генерирует и возвращает ключи шифрования
Выберем случайные простые числа p и q
n = p*q
f = (p-1)(q-1)
e - произвольное число, взаимнопростое с f
Найдем такое d, что d*e = 1 (mod f)
Теперь e, n - параметры открытого ключа, d - закрытый ключ 

Как зашифровать m?
m -> m^e (mod n)

Как расшифровать c?
c -> c^d (mod n)
