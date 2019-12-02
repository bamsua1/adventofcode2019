def calculate_fuel_requirements() -> int:
    total = 0
    with open('input.txt', 'r') as f:
        for mass in f.readlines():
            mass = int(mass.strip('\n'))
            total += (mass // 3) - 2

    return total


if __name__ == '__main__':
    print(calculate_fuel_requirements())