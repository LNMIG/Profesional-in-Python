from datetime import datetime


def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time= datetime.now()
        func(*args, **kwargs)
        end_time= datetime.now()
        elapsed_time= end_time - start_time
        print ('Pasaron ' + str(elapsed_time.total_seconds()) + ' segundos')
    return wrapper


@execution_time
def random_func():
    for _ in range (1, 100000000):
        pass


@execution_time
def suma(a: int, b: int) -> int:
    return a + b


@execution_time
def saludo(nombre= 'Cesar'):
    print ("Hola " + nombre)


random_func()
suma(6, 8)
saludo("Luis")