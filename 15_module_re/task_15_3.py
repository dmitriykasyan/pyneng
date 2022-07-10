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
### Фукция парсинга файла
  """
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

if __name__ == "__main__":
  pprint(parse_cisco_nat_conf('cisco_nat_config.txt'))
"""
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