import os


# Функция получения списка файлов в каталоге и подкаталогах
def lenght_path(directory_file):
    filelist = os.listdir(directory_file)
    fullfilelist = list()
    for my_file in filelist:
        # Получаем полный путь
        fullpath = os.path.join(directory_file, my_file)
        # Проверяем путь является файлом или каталогом
        if os.path.isdir(fullpath):
            fullfilelist = fullfilelist + lenght_path(fullpath)
        else:
            fullfilelist.append(fullpath)
    # Возвращаем список
    return fullfilelist


print('Введите директорию для проверки длины пути к файлам и подкаталогам:')
directory = input()
list_of_files = lenght_path(directory)
# Проверяем список на наличие файлов с длиной пути более 255 символов и записываем результат в файл
for name in list_of_files:
    if len(name) > 255:
        file = open('File&directory_path_more_255.txt', 'a+')
        file.write(name+'\n')
        file.close()
