# -*- coding: utf-8 -*-

ip_addr = input ('Введите IP адрес: ')

check_ip = False

while check_ip == False:
    octets = (ip_addr.split('.'))
    if len(octets) < 4 or len(octets) > 4:
        print ('Адрес содержит не верное число октетов')
        ip_addr = input ('Введите IP адрес: ')
    elif len(octets) == 4:
        for oct_n in octets:
            if oct_n.isdigit() == False:
                print ('{} не является числом'.format(oct_n))
                ip_addr = input ('Введите IP адрес: ')
                break
            elif int(oct_n) <0 or int(oct_n) > 255:
                print ('{} - выходит за рамки ip адреса'.format(oct_n))
                ip_addr = input ('Введите IP адрес: ')
                break
        else:
            print ('IP корректный')
            check_ip = True
            break
    else:
        break
    
print ('IP продолжаем...')
oct_1 = int(ip_addr.split('.')[0])

print (oct_1,type(oct_1))

if ip_addr == '0.0.0.0':
        print ('IP is unassigned')
elif ip_addr == '255.255.255.255':
        print ('IP is local broadcast')
elif oct_1 > 0 and oct_1 < 223:
        print ('IP is unicast')
elif oct_1 > 224 and oct_1 < 239:
        print ('IP is multicast')
else:
        print ('IP is unused')
