T = [
    ['', 'peter', 'emily'],
    ['Lucy', 'Sarah', 'Edwordo'],
    ['James', 'Adam', '']
]


def ser():
    for i in range(0, len(T)):
        for j in range(0, len(T[i])):
            print(f"{T[i][j]} {i} {j}")


def update():
    flag = 'True'
    while flag == 'True':
        for i in range(0, len(T)):
            for j in range(0, len(T[i])):
                if T[i][j] == '':
                    flag = 'False'
                    name = input('Name:')
                    T[i][j] = name
                    print(i, j)
                    print(T)
    print(flag)


update()
