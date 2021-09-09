# -*- coding: utf-8 -*-
"""
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

Предупреждение: в разделе 4 тесты можно легко "обмануть" сделав нужный вывод,
без получения результатов из исходных данных с помощью Python.
Это не значит, что задание сделано правильно, просто на данном этапе сложно иначе
проверять результат.
"""

ospf_route = "      10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0"

ospf_route = ospf_route.strip()
ospf_route = ospf_route.replace(',' , '')
ospf_route = ospf_route.split()

ospf_prefix = ospf_route[0]
ospf_ad_metric = ospf_route[1].strip('[]')
ospf_next_hop = ospf_route[3]
ospf_last_update = ospf_route[4]
ospf_outband_int = ospf_route[5]

print(f'''
{'Prefix':20} {ospf_prefix}
{'AD/Metric':20} {ospf_ad_metric}
{'Next-Hop':20} {ospf_next_hop}
{'Last update':20} {ospf_last_update}
{'Outband interface':20} {ospf_outband_int}
''')

