def roman_to_int(value: str) -> int:
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for index, current in enumerate(value):
        ## if next index < length of value and current value of roman < next value of roman
        if (index + 1) < len(value) and romans[current] < romans[value[index + 1]]:
            total = total - romans[value[index]]
        else:
            total = total + romans[value[index]]

    return total


if __name__ == '__main__':
    example = ['III', 'LVIII', 'CXXIV', 'MCMXCIV']
    for i in example:
        print(f'{i} -> {roman_to_int(i)}')
