import time

def my_gen(max: int):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            aux = n1 + n2
            if aux > max:
                break
            else:
                n1, n2 = n2, aux
                counter += 1
                yield aux

if __name__ == '__main__':
    fibo = my_gen(33)
    for i in fibo:
        print(i)
        time.sleep(0.5)