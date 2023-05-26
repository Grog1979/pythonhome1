# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input('enter lenght: '))
m = int(input('enter width: '))
k = int(input('enter number: '))
x = m * n - k
y = m * n
if y > k and (x % m == 0 or x % n == 0):
  print('yes')
else:  
  print('no')

