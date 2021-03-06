# -*- coding: utf-8 -*-
"""
Задание 4.8

Преобразовать IP-адрес в переменной ip в двоичный формат и вывести на стандартный
поток вывода вывод столбцами, таким образом:
- первой строкой должны идти десятичные значения байтов
- второй строкой двоичные значения

Вывод должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Пример вывода для адреса 10.1.1.1:
10        1         1         1
00001010  00000001  00000001  00000001

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ip = "192.168.3.1"

print (ip)
print ('#' * 40)

ip_oct1 = int(ip.split('.')[0])
ip_oct2 = int(ip.split('.')[1])
ip_oct3 = int(ip.split('.')[2])
ip_oct4 = int(ip.split('.')[3])

print (f'''
{ip_oct1:<10} {ip_oct2:<10} {ip_oct3:<10} {ip_oct4:<10} 
{ip_oct1:>010b} {ip_oct2:>010b} {ip_oct3:>010b} {ip_oct4:>010b}
''')
