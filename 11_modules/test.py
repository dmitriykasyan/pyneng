# -*- coding: utf-8 -*-

from pprint import pprint

net_map={
     ('R1', 'Eth0/0'): ('SW1', 'Eth0/1'),
     ('R2', 'Eth0/0'): ('SW1', 'Eth0/2'),
     ('R2', 'Eth0/1'): ('SW2', 'Eth0/11'),
     ('R3', 'Eth0/0'): ('SW1', 'Eth0/3'),
     ('R3', 'Eth0/1'): ('R4', 'Eth0/0'),
     ('R3', 'Eth0/2'): ('R5', 'Eth0/0'),
     ('SW1', 'Eth0/1'): ('R1', 'Eth0/0'),
     ('SW1', 'Eth0/2'): ('R2', 'Eth0/0'),
     ('SW1', 'Eth0/3'): ('R3', 'Eth0/0'),
     ('SW1', 'Eth0/5'): ('R6', 'Eth0/1')
}

inverse = {}

for key in list(net_map.keys()):
#   print(key)
    for value in net_map.values():
#       print(key,' -- ',value)
        if value not in inverse:
            inverse[value] = [key]
#       else:
#           inverse[value].append(key)

#       inverse[value] = [key]

pprint(net_map)
print (40*'#')
pprint(inverse)

# for key, value in values_keys.items():
    #     if len(value) > 1:
#         print("key {}: We have duplicated values at keys {}".format(key,','.join(map(str, value))))
