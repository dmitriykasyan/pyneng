# -*- coding: utf-8 -*-
"""
Задание 15.3

Создать функцию convert_ios_nat_to_asa, которая конвертирует правила NAT
из синтаксиса cisco IOS в cisco ASA.

Функция ожидает такие аргументы:
- имя файла, в котором находится правила NAT Cisco IOS
- имя файла, в который надо записать полученные правила NAT для ASA

Функция ничего не возвращает.

Проверить функцию на файле cisco_nat_config.txt.

Пример правил NAT cisco IOS
ip nat inside source static tcp 10.1.2.84 22 interface GigabitEthernet0/1 20022
ip nat inside source static tcp 10.1.9.5 22 interface GigabitEthernet0/1 20023

И соответствующие правила NAT для ASA:
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.9.5
 host 10.1.9.5
 nat (inside,outside) static interface service tcp 22 20023

В файле с правилами для ASA:
- не должно быть пустых строк между правилами
- перед строками "object network" не должны быть пробелы
- перед остальными строками должен быть один пробел

Во всех правилах для ASA интерфейсы будут одинаковыми (inside,outside).
"""
import re
from pprint import pprint

def parse_cisco_nat_conf(fname):
  """
  Фукция парсинга файла конфигурации:
  Выделить следующие поля из строк:
  ip, tcp, src_port, dst_port
  """

  with open(fname) as f:
    data = f.read()
    regexp = r'static (\S+) +'\
             r'([\d.]+) +'\
             r'(\d+) +'\
             r'\w+ \S+ +'\
             r'(\d+)'  
    result = [m.groups() for m in re.finditer(regexp,data)]
    # pprint (result)
    return result



def convert_ios_nat_to_asa(src_fname,dst_fname):
  
  asa_template = [
    "object network LOCAL_",
    "host",
    "nat (inside,outside) static interface service"
    ]
  
  data_to_convert = parse_cisco_nat_conf(src_fname)
  with open(dst_fname,'w') as file_write:
    for data in data_to_convert:
      proto, ip, src_port, dst_port = data
      # print (f"{ip},{proto}, {src_port}, {dst_port}")
      for command in asa_template:
        if command.endswith ("LOCAL_"):
          # print(f"{command}{ip}")                             #Test format string
          file_write.write (f"{command}{ip}\n")
        elif command.endswith ("host"):
          file_write.write (f" {command} {ip}\n")
          # print(f" {command} {ip}")                           #Test format string
        elif command.endswith ("service"):
          file_write.write (f" {command} {proto} {src_port} {dst_port}\n")
          # print(f" {command} {proto} {src_port} {dst_port}")  #Test format string
    print('Convert to ASA config is complite!')


convert_ios_nat_to_asa ('cisco_nat_config.txt','res.txt')



"""
### Result parse_cisco_nat_conf
08:44 $ /home/vagrant/venv/pyneng-py3-8/bin/python /home/vagrant/CourseDir/pyneng/15_module_re/task_15_3.py
[('tcp', '10.66.0.13', '995', '995'),
 ('tcp', '10.66.0.21', '20065', '20065'),
 ('tcp', '10.66.0.22', '443', '44443'),
 ('tcp', '10.66.0.23', '2565', '2565'),
 ('tcp', '10.1.2.28', '563', '563'),
 ('tcp', '10.98.1.1', '3389', '3389'),
 ('tcp', '10.14.1.15', '12220', '12220'),
 ('tcp', '10.14.1.169', '25565', '25565'),
 ('tcp', '10.66.0.26', '220', '220'),
 ('tcp', '10.66.37.11', '80', '8080'),
 ('tcp', '10.66.37.13', '10995', '10995'),
 ('tcp', '10.1.2.84', '22', '20022'),
 ('tcp', '10.1.2.66', '22', '20023'),
 ('tcp', '10.1.2.63', '80', '80')]
"""
"""
### Result start task_15_3.py
05:31 $ cat res.txt 
object network LOCAL_10.66.0.13
 host 10.66.0.13
 nat (inside,outside) static interface service tcp 995 995
object network LOCAL_10.66.0.21
 host 10.66.0.21
 nat (inside,outside) static interface service tcp 20065 20065
object network LOCAL_10.66.0.22
 host 10.66.0.22
 nat (inside,outside) static interface service tcp 443 44443
object network LOCAL_10.66.0.23
 host 10.66.0.23
 nat (inside,outside) static interface service tcp 2565 2565
object network LOCAL_10.1.2.28
 host 10.1.2.28
 nat (inside,outside) static interface service tcp 563 563
object network LOCAL_10.98.1.1
 host 10.98.1.1
 nat (inside,outside) static interface service tcp 3389 3389
object network LOCAL_10.14.1.15
 host 10.14.1.15
 nat (inside,outside) static interface service tcp 12220 12220
object network LOCAL_10.14.1.169
 host 10.14.1.169
 nat (inside,outside) static interface service tcp 25565 25565
object network LOCAL_10.66.0.26
 host 10.66.0.26
 nat (inside,outside) static interface service tcp 220 220
object network LOCAL_10.66.37.11
 host 10.66.37.11
 nat (inside,outside) static interface service tcp 80 8080
object network LOCAL_10.66.37.13
 host 10.66.37.13
 nat (inside,outside) static interface service tcp 10995 10995
object network LOCAL_10.1.2.84
 host 10.1.2.84
 nat (inside,outside) static interface service tcp 22 20022
object network LOCAL_10.1.2.66
 host 10.1.2.66
 nat (inside,outside) static interface service tcp 22 20023
object network LOCAL_10.1.2.63
 host 10.1.2.63
 nat (inside,outside) static interface service tcp 80 80
(pyneng-py3-8) 
"""