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

def ping_ip_addresses(ip_address):

    import subprocess

    ip_alive = []
    ip_unreacheble = []

    for i in ip_address:
        my_ping=['ping', '-c', '4', i]

        reply = subprocess.run(my_ping,stdout=subprocess.DEVNULL)

        if reply.returncode == 0:
            ip_alive.append
#           ping_status = 'Alive'
        elif reply.returncode != 0:
#           ping_status ='Unreachable'
            ip_unreacheble.append
        print ('in def' + ip_address, ip_unreacheble)
    return ip_address, ip_unreacheble


check_ip_addresses=['8.8.8.8','192.168.0.1']

result = ping_ip_addresses(check_ip_addresses)
# result = ping_ip_addresses('192.168.1.1')
print ('Host is ' + result)
print (result)
