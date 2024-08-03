# Оператор "with"
# Задача "Найдёт везде"

class WordsFinder():
    def __init__(self, *files):
        self.file_names = files


    def get_all_words(self):
        all_words = dict()
        for file in self.file_names:

            with open(file, 'r', encoding='UTF-8') as f:
                st = f.read().lower().replace('\n',' ')
                lst = ''.join(s for s in st if s.isalpha() or s in (" ","'")).split()
                all_words[file] = lst

        return all_words

    def find(self, word):
        fwords = dict()
        for f, words in self.get_all_words().items():
            if word.lower() in words:
                fwords[f] = words.index(word.lower())+1
        return fwords

    def count(self, word):
        cwords = dict((f, words.count(word.lower())) for f, words
                       in self.get_all_words().items())
        return cwords


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))





