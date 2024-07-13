
def getInput():
    values = input("Enter multiple values separated by spaces: ")
    return list(map(int, values.split()))


def makeReverse(numbers):
    reversed_list = []
    while numbers:
        reversed_list.append(numbers.pop())
    return reversed_list


def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
