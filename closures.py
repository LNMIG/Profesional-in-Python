def make_division_by(n):
    def number_to_be_divided(x):
        return x / n
    return number_to_be_divided

def run():
    make_division_by_23 = make_division_by(23)
    make_division_by_12 = make_division_by(12)
    make_division_by_61 = make_division_by(61)
    division_by_3 =  make_division_by(3)
    division_by_5 =  make_division_by(5)
    division_by_18 =  make_division_by(18)

    print(round(make_division_by_23(856),2))
    print(round(make_division_by_12(1444),2))
    print(round(make_division_by_61(634972),2))
    print(round(division_by_3(18)))
    print(round(division_by_5(100)))
    print(round(division_by_18(54)))

if __name__ == '__main__':
    run()