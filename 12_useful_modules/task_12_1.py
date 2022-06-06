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

def ping_ip_addresses(check_ip_address):

    import subprocess

    ip_alive = []
    ip_unreacheble = []

    for i in check_ip_addresses:
        my_ping=['ping', '-c', '3', i]

        reply = subprocess.run(my_ping,stdout=subprocess.DEVNULL)

        if reply.returncode == 0:
            ip_alive.append(i)
        elif reply.returncode != 0:
            ip_unreacheble.append(i)

    ping_status = (ip_alive,ip_unreacheble)
    return ping_status




check_ip_addresses=['9.9.9.9','8.8.8.8','192.168.0.1']

#result = ping_ip_addresses(check_ip_addresses)
#print (result)

print (ping_ip_addresses(check_ip_addresses))
