ip_addr = input ('введите IP-адрес: ')

check_ip = False
while not check_ip:
    octets = (ip_addr.split('.'))
    print (octets, type(octets))

    if len(octets) < 4 or len(octets) > 4:
        print ('адрес содержит не 4-е октета')
        ip_addr = input ('введите IP-адрес: ')
        break
        
    elif len(octets) == 4:
        for oct_n in octets:
            if oct_n.isdigit() == False:
                print ('{} не является числом'.format(oct_n))
                ip_addr = input ('введите IP-адрес: ')
                check_ip = False
                break
            elif int(oct_n) < 0 or int(oct_n) > 255:
                print ('{} - выходит за рамки ip адреса'.format(oct_n))
                ip_addr = input ('введите IP-адрес: ')
                check_ip = False
                break
            else:
                check_ip = True
#       break

#   ip_addr = input ('введите IP-адрес: ')

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
