"""
Дописать скрипт. Программа принимает имя папки и имя
файла с расширением. Создает папку и создает в ней
файл. Если расширение файла py - записывает в файл
"""

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-dn', '--dir_name', required=True)
parser.add_argument('-fn', '--file_name', required=True)
args = parser.parse_args()
os.mkdir(args.dir_name)
os.chdir(args.dir_name)

with open(args.file_name, 'w') as py_file:
    if '.py' in args.file_name:
        py_file.writelines("def main():\n"
                           "    pass\n"
                           "    \n"
                           "    \n"
                           "if __name__ == '__main__':\n"
                           "    main()\n"
                           )
    else:
        with open(args.file_name, 'w') as file:
            file.close()
