
def policz(zdanie, litera: str):
    l = len(litera)
    print(l)
    if l != 1:
        raise ValueError('zmianna liera musi miec tylko jedna litere')
    else:
        print('wszytko ok')
        return zdanie.count(litera)

policz('ala moa kota', 'a')
