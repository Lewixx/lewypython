from dzien7.try_policz import policz

zdanie = 'ala ma kota'
znak = 'oas'

try:

    znalezione = policz(zdanie, znak)
except ValueError:
    print('wyszedl blad')
    #znak = znak[1]
    #znalezione = policz(zdanie, znak)

print(f'w zdaniu jest {znalezione} znakow')
