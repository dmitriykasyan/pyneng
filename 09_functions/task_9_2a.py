# -*- coding: utf-8 -*-
"""
Задание 9.2a

Сделать копию функции generate_trunk_config из задания 9.2

Изменить функцию таким образом, чтобы она возвращала не список команд, а словарь:
- ключи: имена интерфейсов, вида 'FastEthernet0/1'
- значения: список команд, который надо
  выполнить на этом интерфейсе

Проверить работу функции на примере словаря trunk_config и шаблона trunk_mode_template.

Пример итогового словаря, который должна возвращать функция (перевод строки
после каждого элемента сделан для удобства чтения):
{
    "FastEthernet0/1": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 10,20,30",
    ],
    "FastEthernet0/2": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 11,30",
    ],
    "FastEthernet0/4": [
        "switchport mode trunk",
        "switchport trunk native vlan 999",
        "switchport trunk allowed vlan 17",
    ],
}

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

from pprint import pprint 

trunk_mode_template = [
    "switchport mode trunk",
    "switchport trunk native vlan 999",
    "switchport trunk allowed vlan",
]

trunk_config = {
    "FastEthernet0/1": [10, 20, 30],
    "FastEthernet0/2": [11, 30],
    "FastEthernet0/4": [17],
}


def generate_trunk_config(intf_vlan_mapping, trunk_template):
    """
    Genegate vlan config
    """
    result = {}
    for intf, vlans in intf_vlan_mapping.items():
#       result.append(f'Interface {intf}')
        interface = f'Interface {intf}'
        intf_settings = []
        vlans_str=[]
        for vl in vlans:
            vlans_str.append(str(vl))
        for string in trunk_template:
            if string.endswith('allowed vlan'):
                vl=','.join(vlans_str)
                intf_settings.append(f'{string} {vl}')
            else:
                intf_settings.append(f'{string}')
        result[interface] = intf_settings
    return result


pprint(generate_trunk_config(trunk_config,trunk_mode_template))
