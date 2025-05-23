a = 'AAAAAA'
b = 'BBBBBB'
c = 1.1
string = 'a={ant} b={car} a={ant} c={nome3:.2f}' 
formato = string.format(ant=a, car=b, nome3=c)

print(formato)