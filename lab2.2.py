# Целые числа и числа с плавающей точкой являются одними из самых распространенных в языке Python

number = 9 

print(type(number))   # Вывод типа переменной number 

float_number = 9.0

print(int(float_number))

# Создайте ещё несколько переменных разных типов и осуществите вывод их типов  

c = 42
p = 3.1415
d = 'd'
e = True

print('Values:')

print('c =', c)
print('p =', p)
print('d =', d)
print('e =', e)

print('Types:')

print('c =', type(c))
print('p =', type(p))
print('d =', type(d))
print('e =', type(e))



# Существует множество функций, позволяющих изменять тип переменных.
# Изучите такие функции как int(), float(), str() и последовательно примените их к переменным, созданным ранее.

c = str(c)
p = int(p)
d = int(d, 16)
e = int(e)


print('After convertion')

print('Values:')

print('c =', c)
print('p =', p)
print('d =', d)
print('e =', e)

print('Types:')

print('c =', type(c))
print('p =', type(p))
print('d =', type(d))
print('e =', type(e))