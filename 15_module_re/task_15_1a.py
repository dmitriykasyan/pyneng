# -*- coding: utf-8 -*-
"""
Задание 15.1a

Скопировать функцию get_ip_from_cfg из задания 15.1 и переделать ее таким образом,
чтобы она возвращала словарь:
* ключ: имя интерфейса
* значение: кортеж с двумя строками:
  * IP-адрес
  * маска

В словарь добавлять только те интерфейсы, на которых настроены IP-адреса.

Например (взяты произвольные адреса):
{'FastEthernet0/1': ('10.0.1.1', '255.255.255.0'),
 'FastEthernet0/2': ('10.0.2.1', '255.255.255.0')}

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла config_r1.txt.

Обратите внимание, что в данном случае, можно не проверять корректность IP-адреса,
диапазоны адресов и так далее, так как обрабатывается вывод команды,
а не ввод пользователя.

"""
from pprint import pprint
import re

def get_ip_from_cfg(filename):


    result = []
#   regex = r'^\s+ip\ address\s+(?P<ip>(\d+\.){3}(\d+))\s+(?P<mask>(\d+\.){3}(\d+))'
    regex = (r'\s+ip\ address (?P<ip>(\d+\.){3}(\d+))'
             r'\s+'
             r'(?P<mac>(\d+\.){3}(\d+))')

    with open(filename) as file:
        for line in file:
            match = re.match(regex,line)

            if match:
#               res_regex = f"{match.group('ip')},{match.group('mask')}"
#               res_line = tuple(res_regex.split(','))
#               result.append(res_line)
                result.append(match.group('ip','mac'))
        return result


if __name__ == '__main__':
    pprint (get_ip_from_cfg('config_r1.txt'))

