# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

def get_ping_status(ip_address):

    import subprocess

    my_ping=['ping', '-c', '4', ip_address]
    
    reply = subprocess.run(my_ping,stdout=subprocess.DEVNULL)
    
    if reply.returncode == 0:
        ping_status = 'Alive'
        return ping_status
#       print('Alive')
    else:
        ping_status ='Unreachable'
        return ping_status
#       print('Unreachable')
#   return ping_status

ping_status = ''
get_ping_status('8.8.8.8')
print (ping_status)
