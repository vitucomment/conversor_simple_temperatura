def text_formatado(msg):
    print('=-'*30)
    print(f'{msg:^60}')
    print('=-'*30)


def menu():
    text_formatado('Conversão de Temperaturas: ')
    print('Celcius      --> C\n'
          'Fahrenheit   --> F\n'
          'Kelvin       --> K')
menu()


escolha1 = input('Converter de: ').upper()
while escolha1 not in ('C', 'F', 'K'):
    print('Você deve escolher entre C para Celcius, F para Fahrenheit ou K para Kelvin')
    escolha1 = input('Converter de: ').upper()


escolha2 = input('Para: ').upper()
while escolha2 not in ('C', 'F', 'K'):
    print('Você deve escolher entre C para Celcius, F para Fahrenheit ou K para Kelvin')
    escolha2 = input('Para: ').upper()


temp = int(input(f'Digite a temperatura em {escolha1}: '))


if escolha1 == 'C' and escolha2 == 'F':
    resul = (temp * 9/5) + 32
    form = 'Convertendo de Celcius para Fahrenheit...'
if escolha1 == 'C' and escolha2 == 'K':
    resul = (temp + 273.15)
    form = 'Convertendo de Celcius para Kelvin...'
if escolha1 == 'C' and escolha2 == 'C':
    resul = temp
    form = 'Convertendo de Celcius para Celcius...'

if escolha1 == 'F' and escolha2 == 'C':
    resul = (temp - 32) * 5/9
    form = 'Convertendo de Fahrenheit para Celcius...'
if escolha1 == 'F' and escolha2 == 'K':
    resul = (temp - 32) * 5/9 + 273.15
    form = 'Convertendo de Fahrenheit para Kelvin...'
if escolha1 == 'F' and escolha2 == 'F':
    resul = temp
    form = 'Convertendo de Fahrenheit para Fahrenheit...'

if escolha1 == 'K' and escolha2 == 'C':
    resul = (temp - 273.15)
    form = 'Convertendo de Kelvin para Celcius...'
if escolha1 == 'K' and escolha2 == 'F':
    resul = (temp - 273.15) * 9/5 + 32
    form = 'Convertendo de Kelvin para Fahrenheit...'
if escolha1 == 'K' and escolha2 == 'K':
    resul = temp
    form = 'Convertendo de Kelvin para Kelvin...'

print(form)
print(round(resul, 2), escolha2)