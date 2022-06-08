# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
def convert_ranges_to_ip_list(ip_range):
    import ipaddress

    #ip_range = ['192.168.12.1','10.10.0.7-10','10.20.30.1-10.20.30.5']
    ip_result = []
    for ip_addr in ip_range:
        try:
            ip = ipaddress.ip_address(ip_addr)
    #       print("IP address {} is valid.".format(ip_addr, ip))
    #       print (ip_addr)
            ip_result.append(ip_addr)
        except ValueError:
    #       print("IP address {} is not valid".format(ip_addr))

            if len(ip_addr.split('.')) == 4:
                oct1,oct2,oct3,oct4 = ip_addr.split('.')
                if '-' in  oct4:
    #                print ('oct4 is range')
                     range_start,range_end = oct4.split('-')
    #                print ('range from '+range_start+' to '+range_end)
                     for oct4_r in range(int(range_start),int(range_end)+1):
                         result = f'{oct1}.{oct2}.{oct3}.{oct4_r}'
    #                    print (f'{oct1}.{oct2}.{oct3}.{oct4_r}')
    #                    print (result)
                         ip_result.append(result)
            else:
                ip_addr_start, ip_addr_end = ip_addr.split('-')
    #           print (f'{ip_addr_start}  --  {ip_addr_end}')
                if ipaddress.ip_address(ip_addr_end) > ipaddress.ip_address(ip_addr_start):
                    ip_st_oct1, ip_st_oct2, ip_st_oct3, ip_st_oct4 = ip_addr_start.split('.')
                    ip_end_oct1, ip_end_oct2, ip_end_oct3, ip_end_oct4 = ip_addr_end.split('.')
#                   for oct4_r in range(int(ip_st_oct4),int(ip_end_oct4)+1):
#                       result = f'{ip_st_oct1}.{ip_st_oct2}.{ip_st_oct3}.{oct4_r}'
#    #                  print (result)
#    #                  print (f'{ip_st_oct1}.{ip_st_oct2}.{ip_st_oct3}.{oct4_r}')
#                       ip_result.append(result)
                    a = generate_ip_range(ip_st_oct4,ip_end_oct4,ip_st_oct1,ip_st_oct2,ip_st_oct3)
                    ip_result.extend(a)
                else:
                    exit
    return ip_result

def generate_ip_range(ip_start,ip_end,oct_1,oct_2,oct_3):

#   ip_n_start = '1'
#   ip_n_end = '3'
#   oct1 = '192'
#   oct2 = '168'
#   oct3 = '10'

    res_gen_ip = []

    for oct_4 in range(int(ip_n_start),int(ip_n_end)+1):
        result = f'{oct_1}.{oct_2}.{oct_3}.{oct_4}'
        print (result)
        res_generate_ip_ip.append(result)

    return res_generate_ip



ip_list = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
print (convert_ranges_to_ip_list(ip_list))
