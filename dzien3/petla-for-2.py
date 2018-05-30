#wypsiac liczby od 0 do 20 poza tymi podzielnymi przez 4

#while
i=1

while i <= 20:
    if i % 4 != 0:
        print(i)
    i = i + 1

for j in range(20):
    if j % 4 != 0:
        print(j)
