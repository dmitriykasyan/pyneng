# -*- coding: utf-8 -*-
"""
Задание 15.2

Создать функцию parse_sh_ip_int_br, которая ожидает как аргумент
имя файла, в котором находится вывод команды show ip int br

Функция должна обрабатывать вывод команды show ip int br и возвращать такие поля:
* Interface
* IP-Address
* Status
* Protocol

Информация должна возвращаться в виде списка кортежей:
[('FastEthernet0/0', '10.0.1.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.2.1', 'up', 'up'),
 ('FastEthernet0/2', 'unassigned', 'down', 'down')]

Для получения такого результата, используйте регулярные выражения.

Проверить работу функции на примере файла sh_ip_int_br.txt.

"""
import re
from pprint import pprint

def parse_sh_ip_int_br(fname):
  with open(fname) as f:
    data = f.read()

    regexp =  r'(\S+) +'\
              r'([\d.]+) +'\
              r'\w+ \w+ +'\
              r'(up|down|administratively down) +'\
              r'(up|down)'

    result = [m.groups() for m in re.finditer(regexp,data)]
    return result


if __name__ == '__main__':
  pprint (parse_sh_ip_int_br('sh_ip_int_br.txt'))

'''
vagrant@PyNEng: $  [main|✚ 1⚑ 1] 
03:39 $ /home/vagrant/venv/pyneng-py3-8/bin/python /home/vagrant/CourseDir/pyneng/15_module_re/task_15_2.py
[('FastEthernet0/0', '15.0.15.1', 'up', 'up'),
 ('FastEthernet0/1', '10.0.12.1', 'up', 'up'),
 ('FastEthernet0/2', '10.0.13.1', 'up', 'up'),
 ('Loopback0', '10.1.1.1', 'up', 'up'),
 ('Loopback100', '100.0.0.1', 'up', 'up')]
'''