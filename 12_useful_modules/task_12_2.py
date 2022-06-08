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
import ipaddress

#ip_range = ['192.168.12.1','10.10.0.1-10']

#for ip_addr in ip_range:

ip_addr = '10.20.30.1-10'

#oct1,oct2,oct3,oct4 = ip_addr.split('.')
#
#if '-' in  oct4:
#    print ('oct4 is range')
#    range_start,range_end = oct4.split('-')
#    print ('range from '+range_start+' to '+range_end)
##   print (list(range(int(range_start),int(range_end)+1)))
#    for oct4_r in range(int(range_start),int(range_end)+1):
#        print (oct1+'.'+oct2+'.'+oct3+'.'+str(oct4_r))
#        #сделать f строку
#else:
#    print ('oct4 is`t range')
#    print (ip_addr)

try:
    ip = ipaddress.ip_address(ip_addr)
    print("IP address {} is valid.".format(ip_addr, ip))
except ValueError:
    print("IP address {} is not valid".format(ip_addr))
    oct1,oct2,oct3,oct4 = ip_addr.split('.')
    if '-' in  oct4:
	    print ('oct4 is range')
	    range_start,range_end = oct4.split('-')
	    print ('range from '+range_start+' to '+range_end)
	#   print (list(range(int(range_start),int(range_end)+1)))
	    for oct4_r in range(int(range_start),int(range_end)+1):
	        print (oct1+'.'+oct2+'.'+oct3+'.'+str(oct4_r))
