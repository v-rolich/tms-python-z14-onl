# Дописать скрипт. Программа принимает имя папки и имя
# файла. Создает папку и создает в ней файл.
import os
import sys
import shutil

print(sys.argv)

file_name = sys.argv[2]
file = open(file_name, 'w')
file.write('Text file')
os.makedirs(sys.argv[1])
shutil.move(file_name, sys.argv[1])
file.close()
