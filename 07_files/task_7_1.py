# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

result = {
    'Prefix' : None,
    'AD/Metric' : None,
    'Next-Hop' : None,
    'Last update' : None,
    'Outbound Interface' : None
}

with open('ospf.txt','r') as f:
    for line in f:
### use vars
#       pref=line.split()[1]
#       metric=line.split()[2].strip('[]')
#       hop=line.split()[4][:-1]
#       upd=line.split()[5][:-1]
#       intf=line.split()[6]

#         print(f'''
# prefix {pref:<12}
# AD/Metric {metric:<12}
# Next-Hop {hop:<12}
# Last update {upd:<12}
# Outbound Interface {intf:<12}
#             ''')
### use dict
        result.update({'Prefix': line.split()[1]})
        result.update({'AD/Metric' : line.split()[2].strip('[]')})
        result.update({'Next-Hop' : line.split()[4][:-1]})
        result.update({'Last update' : line.split()[5][:-1]})
        result.update({'Outbound Interface' : line.split()[6]})
        
        for i, j in result.items():
            print (f'{i:20} {j:<}')
        print ('\n')
