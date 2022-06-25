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

    result = {}
    regex = ('!.*?interface (?P<intf>\S+).+? ip address (?P<ip>\S+) (?P<mask>\S+).*?!')

    with open(filename) as file:
        data = file.read()
        match = re.finditer(regex, data, re.DOTALL)
        for m in match:
            # print (m.groups()) 
            result[m.group('intf')] = m.group('ip', 'mask')
        return result


if __name__ == '__main__':
    pprint (get_ip_from_cfg('config_r1.txt'),sort_dicts=0)

"""
{'Loopback0': ('10.1.1.1', '255.255.255.255'),
 'Ethernet0/0': ('10.0.13.1', '255.255.255.0'),
 'Ethernet0/2': ('10.0.19.1', '255.255.255.0')}
"""
