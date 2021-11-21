# Дописать скрипт. Программа принимает имя папки и имя
# файла. Создает папку и создает в ней файл.
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dn', '--dir-name',
                    required=True)
parser.add_argument('-fn', '--file-name',
                    required=True)

args = parser.parse_args()
print(args)
os.mkdir(args.dir_name)
os.chdir(args.dir_name)
a = open(args.file_name, 'w')
