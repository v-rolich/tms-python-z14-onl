# Создать скрипт, который принимает имя папки и создает
# ее рядом со скриптом
import os
import sys

print(sys.argv)

os.makedirs(sys.argv[1])
