"""
Дописать скрипт. Программа принимает имя папки и имя
файла. Создает папку и создает в ней файл.
"""

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dn', '--dir_name', required=True)
parser.add_argument('-fn', '--file_name', required=True)
args = parser.parse_args()
os.mkdir(args.dir_name)
os.chdir(args.dir_name)

with open(args.file_name, 'w') as file:
    file.close()
