# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""

access_template = [
    "switchport mode access",
    "switchport access vlan {}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {}",
]

port_settings = {
    "access":access_template,
    "trunk":trunk_template}

mode = input('Введите режим работы интерфейса (access/trunk): ')

# add new value in list
access_template.append('номер VLAN:')
trunk_template.append('разрешенные VLANы:')

interface = input('Введите тип и номер интерфейса: ')
vlan = input('Введите ' + list(port_settings[mode])[-1] + ' ') #read last value from list

#remove last value from list
access_template.pop()
trunk_template.pop()

print('\n' + 'Interface ' + interface) 
port_print=str(port_settings[mode]).strip('[]').strip("''").replace("', '","\n")

print(port_print.format(vlan))
