import criteria
from random import randint

def get_rand():
    a = {}
    count = int(input("Type in the number of options: "))
    x_min, x_max = int(input('x_min: ')), int(input('x_max: '))
    y_min, y_max = int(input('y_min: ')), int(input('y_max: '))
    for i in range (1, count+1):
        a[i] = [randint(x_min, x_max), randint(y_min, y_max)]
        a[i].extend(('+', '+', '+', '+'))
    return a


if __name__ == "__main__":
    a = get_rand()
    a = criteria.pareto(a)
    criteria.render(a)
    criteria.plot(a)

    input('Press ENTER to exit...')
    print()