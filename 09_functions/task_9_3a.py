# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию: добавить поддержку конфигурации, когда настройка access-порта
выглядит так:
    interface FastEthernet0/20
        switchport mode access
        duplex auto

То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
Пример словаря:
    {'FastEthernet0/12': 10,
     'FastEthernet0/14': 11,
     'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает
как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from pprint import pprint


def get_int_vlan_map(config_filename):
    """
    Parsing config file
    """
    with open (config_filename) as f:
        dict_access = {}
        dict_trunk = {}
        for line in f:
            if 'interface' in line:
                intf = line.split()[-1]
            elif 'access vlan' in line:
                vlan_access = int(line.split()[-1])
                dict_access[intf]=vlan_access
            elif 'mode access' in line:
                vlan_access = 1
                dict_access[intf]=vlan_access
            elif 'allowed vlan' in line:
                allowed_vlan = [int(item) for item in line.split()[-1].split(',')]
                dict_trunk[intf]=allowed_vlan
    return dict_access, dict_trunk


pprint(get_int_vlan_map ('config_sw2.txt'))
