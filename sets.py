# [1, 1, 2, 2, 4] -> [1, 2, 4]

# Method ONE
# def remove_duplicate(with_duplicates):
#     without_duplicates = []
#     for i in with_duplicates:
#         if i not in without_duplicates:
#             without_duplicates.append(i)
#     return without_duplicates

# Method TWO
# def remove_duplicate(with_duplicates):
#     aux = set(with_duplicates)
#     without_duplicates = [i for i in aux]
#     return without_duplicates

# Method THREE
def remove_duplicate(with_duplicates):
    without_duplicates = set(with_duplicates)
    return list(without_duplicates)

def run():
    with_duplicates = [1, 1, 2, 2, 4]
    print(remove_duplicate(with_duplicates))


if __name__ == '__main__':
    run()