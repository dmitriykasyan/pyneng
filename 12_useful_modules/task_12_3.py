# -*- coding: utf-8 -*-
"""
Задание 12.3

Создать функцию print_ip_table, которая отображает таблицу доступных
и недоступных IP-адресов.

Функция ожидает как аргументы два списка:
* список доступных IP-адресов
* список недоступных IP-адресов

Результат работы функции - вывод на стандартный поток вывода таблицы вида:

Reachable    Unreachable
-----------  -------------
10.1.1.1     10.1.1.7
10.1.1.2     10.1.1.8
             10.1.1.9

"""
import task_12_1 as chk_ip
from tabulate import tabulate

columns = ['Reacheble','Unreacheble']
my_ip = ['8.8.8.8','87.250.250.242','192.168.100.1','192.168.1.1','192.168.2.1']

def_res = chk_ip.ping_ip_addresses(my_ip)

result = {columns[n]: def_res[n] for n in range(len(columns))}
