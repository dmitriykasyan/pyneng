# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт: Скрипт не должен выводить на стандартрый поток вывода команды,
в которых содержатся слова из списка ignore.

При этом скрипт также не должен выводить строки, которые начинаются на !.

Проверить работу скрипта на конфигурационном файле config_sw1.txt.
Имя файла передается как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
with open (argv[1]) as f:
    for line in f:
        if line.startswith('/n') is not True and \
           line.startswith('!') is not True and \
           line.startswith(ignore[0]) is not True and \
           line.startswith(ignore[1]) is not True and \
           line.startswith(ignore[2]) is not True:
            print(line.strip('\n'))
#       for exept in ignore:
#           if line.startswith('/n') is not True and \
#              line.startswith('!') is not True and \
#              line.startswith(exept) is not True:
#               print(line.strip('/n'))
#               pass
#           else:
#               print(line.strip('/n'))
