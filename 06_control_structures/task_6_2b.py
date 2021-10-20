# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip_addr = input ('введите IP-адрес: ')

check_ip = False
while not check_ip:
    octets = (ip_addr.split('.'))
    print (octets, type(octets))

    if len(octets) < 4:
        print ('адрес содержит меньше 4-х чисел')
    elif len(octets) == 4:
        for oct_n in octets:
            if oct_n.isdigit() == False:
                print ('{} не является числом'.format(oct_n))
            elif int(oct_n) < 0 or int(oct_n) > 255:
                print ('{} - выходит за рамки ip адреса'.format(oct_n))
                break
    else:
        check_ip = True
        break

    ip_addr = input ('введите IP-адрес: ')

oct_1 = int(ip_addr.split('.')[0])

if ip_addr == '0.0.0.0':
    print ('IP is unassigned')
elif ip_addr == '255.255.255.255':
    print ('IP is local broadcast')
elif oct_1 > 1 and oct_1 < 223:
    print ('IP is unicast')
elif oct_1 > 224 and oct_1 < 239:
    print ('IP is multicast')
else:
    print ('IP is unused')
