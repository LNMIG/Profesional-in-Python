def decorator(func):
    def wrapper(texto):
        return func(texto).upper()
    return wrapper

def messaje1(nome):
    return f'{nome}, recibiste un mensaje'
messaje1 = decorator(messaje1)

@decorator # sugar sintax
def messaje2(nome):
    return f'{nome}, recibiste un mensaje'

def run():
    print(messaje1('Luiggi'))
    print(messaje2('Cesar'))

if __name__ == '__main__':
    run()