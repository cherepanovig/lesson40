# Цель: освоить механизмы работы итераторов и описания методов __next__ и __iter__.
# Закрепить навык создания  и выбрасывания исключений.

class StepValueError(ValueError):
    pass


class Iterator:

    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
            raise StepValueError('Шаг не может быть равен 0')
        if step > 0 and start > stop:
            raise StepValueError('Итерация невозможна так как старт больше чем стоп, а шаг по умолчанию = +1')

    def __iter__(self):
        self.pointer = self.start  # Сбрасываем pointer на начальное значение start
        return self

    def __next__(self):
        if ((self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop)):
            #print("Печатаем StopIteration")
            raise StopIteration("Итерация закончена")
        result = self.pointer # Сохраняем текущее значение pointer в переменной result.
        self.pointer += self.step # Изменяем значение pointer на величину шага
        #print(result)
        return result


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
# except StepValueError:  # Не понял зачем здесь переопределять сообщение исключения, если мы его уже создали:
# 'Шаг не может быть равен 0'
#     print('Шаг указан неверно')
except StepValueError as exc:
    print(exc)

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
#iter5 = Iterator(10, 1)

#print()
for i in iter2:
    print(i, end=' ')  # параметр end функции print() позволяет задать любой символ или строку, которая будет
    # добавлена после вывода значения
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
# for i in iter5:
#     print(i, end=' ')
try:
    iter5 = Iterator(10, 1)
    for i in iter5:
        print(i, end=' ')
except StepValueError as exc:
    print(exc)
