def total(*numbers):
    print(sum(numbers))

total(1, 2, 3, 4)


def profile(**data):
    for key, value in data.items():
        print(key, value)

profile(name="Alua", age=18)