import tempfile
import sys

class FileWithMagicMethods():
    def __init__(self, path): #инициализируем экземпляр класса.
        self.path = path
        self.file = open(self.path, 'r+')
        self.counter = 0
        self.end = len(open(self.path, 'r').readlines())
    def write(self, stroka): #реализуем метод записи строки в файл.
        with open(self.path, 'w') as file: #открываем файл на запись.
            file.write(stroka) #пишем строку
    def __add__(self, other): #переопределяем оператор сложения
        with open(self.path, 'r') as f1: #открываем первый файл на чтение
            with open(other.path, 'r') as f2: #открываем второй файл на чтение
                with tempfile.TemporaryDirectory() as tmpdirname: #создаем временную директорию
                    with open(tmpdirname + '\\' + 'newfile.txt', 'a') as f3: # в которой создаем файл
                        f3.write(str(f1))
                        f3.write(str(f2))
                        return f3

    def __iter__(self):
        return self
    def __next__(self):
        while self.counter < self.end:
            self.counter += 1
            g = self.file.readline()
            return g
        raise StopIteration





a = FileWithMagicMethods(r'C:\Users\mkirichenko.M-PR\PycharmProjects\coursera\1.txt')
b = FileWithMagicMethods(r'C:\Users\mkirichenko.M-PR\PycharmProjects\coursera\2.txt')
c = a+b
print(c)

for line in FileWithMagicMethods(r'C:\Users\mkirichenko.M-PR\PycharmProjects\coursera\1.txt'):
    print(line)


