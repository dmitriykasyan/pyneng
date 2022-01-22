# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
print(argv[1], argv[2])
with open(argv[1]) as src, open(argv[2],'w') as dest:
    for line in src:
        if line.startswith('/n') is not True and \
           line.startswith('!') is not True and \
           line.startswith(ignore[0]) is not True and \
           line.startswith(ignore[1]) is not True and \
           line.startswith(ignore[2]) is not True:
            print(line.strip('\n'))
            dest.write(line)
