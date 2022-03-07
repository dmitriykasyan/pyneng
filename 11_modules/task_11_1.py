# -*- coding: utf-8 -*-
"""
Задание 11.1

Создать функцию parse_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

У функции должен быть один параметр command_output, который ожидает как аргумент
вывод команды одной строкой (не имя файла). Для этого надо считать все содержимое
файла в строку, а затем передать строку как аргумент функции (как передать вывод
команды показано в коде ниже).

Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:

    {("R4", "Fa0/1"): ("R5", "Fa0/1"),
     ("R4", "Fa0/2"): ("R6", "Fa0/0")}

В словаре интерфейсы должны быть записаны без пробела между типом и именем.
То есть так Fa0/0, а не так Fa 0/0.

Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt. При этом функция должна
работать и на других файлах (тест проверяет работу функции на выводе
из sh_cdp_n_sw1.txt и sh_cdp_n_r3.txt).

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
from pprint import pprint

#def parse_cdp_neighbors(command_output):
#    """
#    Тут мы передаем вывод команды одной строкой потому что именно в таком виде будет
#    получен вывод команды с оборудования. Принимая как аргумент вывод команды,
#    вместо имени файла, мы делаем функцию более универсальной: она может работать
#    и с файлами и с выводом с оборудования.
#    Плюс учимся работать с таким выводом.
#    """
#
#
#if __name__ == "__main__":
#    with open("sh_cdp_n_sw1.txt") as f:
#        print(parse_cdp_neighbors(f.read()))

dict_result = {}
#key = ()
#temp_keys = []
#item_key = ''

with open('sh_cdp_n_sw1.txt') as f:
    for string in f:
        #print (string)
        if 'cdp' in string:
#           print (string.split('>')[0])
#           item_key.append(string.split('>')[0])
            item_key = (string.split('>')[0])
#           print (string.split('>')[0])
        elif 'Eth' in string:
#           print (string.split())
#           item_key.append(string.split()[0])
#           print (tuple(item_key))
            name, l_t_intf, l_intf, *other, r_t_intf, r_intf = string.split()
            print (f'{item_key:4}{l_t_intf:6}{l_intf:6}--- {name:6}{r_t_intf:6}{r_intf}')
#           print (type(item_key),type(l_t_intf),type(l_intf),type(name),type(r_t_intf),type(r_intf))
#           temp_keys=append()item_key,l_t_intf+l_intf
#           print (key)
            dict_result[tuple([item_key, f'{l_t_intf}{l_intf}'])]=tuple([name, f'{r_t_intf}{r_intf}'])
    pprint (dict_result)
