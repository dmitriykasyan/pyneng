# -*- coding: utf-8 -*-

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

inv_map = {v: k for k, v in net_map.items()}

print (net_map)
print (40*'=')
print (inv_map)
