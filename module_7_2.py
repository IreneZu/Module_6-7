# Позиционирование в файле
# Задача "Записать и запомнить"

def custom_write(file_name, strings):
    strings_positions = dict()

    with open(file_name, 'w', encoding='UTF-8') as file_w:
        i = 0
        for s in strings:
            i += 1
            byt = file_w.tell()
            strings_positions.update({(i, byt): s})
            file_w.write(s + '\n')

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
