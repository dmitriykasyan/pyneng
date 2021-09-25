# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv

source=input('Введите IP адрес в формате: 10.1.1.0/24  ')

source_list=source.replace('/', '.').split('.')

ip_oct1=int(source_list[0])
ip_oct2=int(source_list[1])
ip_oct3=int(source_list[2])
ip_oct4=int(source_list[3])
mask=int(source_list[4])

print('\n')
print (f'''
Network:
{ip_oct1:<10} {ip_oct2:<10} {ip_oct3:<10} {ip_oct4:<10} 
{ip_oct1:>010b} {ip_oct2:>010b} {ip_oct3:>010b} {ip_oct4:>010b} 
      ''')

bit_mask='1' * mask + '0' * (32-mask)

bit_mask_oct1=bit_mask[:8]
bit_mask_oct2=bit_mask[8:16]
bit_mask_oct3=bit_mask[16:24]
bit_mask_oct4=bit_mask[24:]

bit_mask_1=int(bit_mask_oct1,2)
bit_mask_2=int(bit_mask_oct2,2)
bit_mask_3=int(bit_mask_oct3,2)
bit_mask_4=int(bit_mask_oct4,2)

print (f'''
Mask:
/'''+str(mask)+f'''
{bit_mask_1:<10} {bit_mask_2:<10} {bit_mask_3:<10} {bit_mask_4:<10} 
{bit_mask_oct1:<10} {bit_mask_oct2:<10} {bit_mask_oct3:<10} {bit_mask_oct4:<10} 
''')
