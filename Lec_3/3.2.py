# Модульность
# Вы когда-нибудь задавались вопрос, как например работает функция .append 
# Это же точно такая же функция, как и sumNumbers(n), но мы ее нигде не создаем, 
# все дело в том что, это функция автоматически срабатывает и чтобы ей пользоваться 
# ничего дополнительно писать не надо. Представьте себе такую ситуацию, что Вы 
# создаете огромный проект и у Вас имеется большое количество функций, к примеру 
# 5 функций работают со словарями, 18 со списками и тд. и у каждой функции свой алгоритм, 
# но их объединяет работа с одной коллекцией данных. Согласитесь неудобно работать в таком 
# большом файле, где около 80 функций, очень легко потеряться и на перемотку кода Вы будете 
# терять драгоценное время. Решение данной проблемы есть. Давайте будем создавать отдельные 
# файлы, где будут находиться только функции, и эти функции при необходимости вызывать из главного файла.


# 1. function_file.py (Новый Python файл, в котором находятся функция f(x)) 
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    return # выход из функции