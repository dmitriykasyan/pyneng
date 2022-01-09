# -*- coding: utf-8 -*-
"""
Задание 6.3

В скрипте сделан генератор конфигурации для access-портов.
Сделать аналогичный генератор конфигурации для портов trunk.

В транках ситуация усложняется тем, что VLANов может быть много, и надо понимать,
что с ними делать (добавлять, удалять, перезаписывать).

Поэтому в соответствии каждому порту стоит список и первый (нулевой) элемент списка
указывает как воспринимать номера VLAN, которые идут дальше.

Пример значения и соответствующей команды:
* ['add', '10', '20'] - команда switchport trunk allowed vlan add 10,20
* ['del', '17'] - команда switchport trunk allowed vlan remove 17
* ['only', '11', '30'] - команда switchport trunk allowed vlan 11,30

Задача для портов 0/1, 0/2, 0/4, 0/5, 0/7:
- сгенерировать конфигурацию на основе шаблона trunk_template
- с учетом ключевых слов add, del, only

Код не должен привязываться к конкретным номерам портов. То есть,
если в словаре trunk будут другие номера интерфейсов, код должен работать.

Для данных в словаре trunk_template вывод на
стандартный поток вывода должен быть таким:
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20
interface FastEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17
interface FastEthernet0/5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,21
interface FastEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30


Ограничение: Все задания надо выполнять используя только пройденные темы.
На стандартный поток вывода надо выводить только команды trunk настройки,
а access закомментировать.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access = {"0/12": "10", "0/15": "11", "0/16": "17", "0/17": "150"}
trunk = {
    "0/1": ["add", "10", "20"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
    "0/5": ["add", "10", "21"],
    "0/7": ["only", "30"],
}

intf = input ('Введите номер интерфейса: ')
# vlan = input('Введите номер vlan: ')

#### check intf 
if intf in access :
    print('Интерфейс в access списке')
#### generate config for access port
    for intf, vlan in access.items():   
        print("interface FastEthernet " + intf)
        for command in access_template:
            if command.endswith("access vlan"):
                print(f" {command} {vlan}")
            else:
                print(f" {command}")
#### generate congfig for trunk port
elif intf in trunk:
    for intf, vlan in trunk.items():
        print("interface FastEthernet " + intf)
        vlan_attr = len(vlan)
        for command in trunk_template:
            if command.endswith("allowed vlan") and vlan_attr == 3:
                print(f" {command} " + vlan[0] + ' ' + vlan[vlan_attr-1] + ',' + vlan[vlan_attr-2])
            elif command.endswith("allowed vlan"):
                print(f" {command} " + vlan[0] + ' ' + vlan[vlan_attr-1])
            else:
                print(f" {command}")
else:
    print(intf, 'отсуствует в списке')

    
    # for intf, vlan in access.items():
        # print("interface FastEthernet" + intf)
            # for command in access_template:
                # if command.endswith("access vlan"):
                    # print(f" {command} {vlan}")
                # else:
                    # print(f" {command}")