# -*- coding: utf-8 -*-
"""
Задание 9.1a

Сделать копию функции generate_access_config из задания 9.1.

Дополнить скрипт: ввести дополнительный параметр, который контролирует будет ли
настроен port-security
 * имя параметра 'psecurity'
 * значение по умолчанию None
 * для настройки port-security, как значение надо передать список команд
   port-security (находятся в списке port_security_template)

Функция должна возвращать список всех портов в режиме access с конфигурацией
на основе шаблона access_mode_template и шаблона port_security_template,
если он был передан.
В конце строк в списке не должно быть символа перевода строки.


Проверить работу функции на примере словаря access_config, с генерацией конфигурации
port-security и без.

Пример вызова функции:
print(generate_access_config(access_config, access_mode_template))
print(generate_access_config(access_config, access_mode_template, port_security_template))

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from pprint import pprint

access_mode_template = [
    "switchport mode access",
    "switchport access vlan",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

port_security_template = [
    "switchport port-security maximum 2",
    "switchport port-security violation restrict",
    "switchport port-security",
]

access_config = {"FastEthernet0/12": 10, "FastEthernet0/14": 11, "FastEthernet0/16": 17}


#def generate_access_config(intf_vlan_mapping, access_template): #, psecurity = False
def generate_access_config(intf_vlan_mapping, access_template, psecurity = False):
    """
    intf_vlan_mapping - словарь с соответствием интерфейс-VLAN такого вида:
        {'FastEthernet0/12':10,
         'FastEthernet0/14':11,
         'FastEthernet0/16':17}
    access_template - список команд для порта в режиме access

    Возвращает список всех портов в режиме access с конфигурацией на основе шаблона
    """
    generate_access_config_list = []
    for intf, vlan in intf_vlan_mapping.items():
        print ('Interface ', intf)
        generate_access_config_list.append(f'Interface {intf}')
        for string_access in access_template:
            if string_access.startswith('switchport access'):
                print (string_access + ' ',vlan)
                generate_access_config_list.append(f'{string_access} {vlan}')
            else:
                print (string_access)
                generate_access_config_list.append(f'{string_access}')
        if psecurity != False:
            for item_sec in psecurity:
                print (item_sec)
                generate_access_config_list.append(f'{item_sec}')

    return generate_access_config_list

#intf_vlan_mapping = access_config
generate_access_config(access_config, access_mode_template, port_security_template)
print(40*'=')
generate_access_config(access_config, access_mode_template)

pprint(generate_access_config)


