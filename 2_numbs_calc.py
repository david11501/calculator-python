def input_number(prompt):
    """Read a float from input with validation."""
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print("Invalid number, please try again.")


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "Error: division by zero"


def multiply(n1, n2):
    return n1 * n2


def subtract(n1, n2):
    return n1 - n2


def add(n1, n2):
    return n1 + n2


def all_ops(n1, n2):
    return {
        "multiply": multiply(n1, n2),
        "add": add(n1, n2),
        "division": divide(n1, n2),
        "difference": subtract(n1, n2),
    }


def print_help():
    print("Available commands:")
    print("  multiply  - multiply the two numbers")
    print("  add       - add the two numbers")
    print("  difference- subtract the second from the first")
    print("  division  - divide the first by the second")
    print("  all       - show results of all operations")
    print("  change    - change the two numbers")
    print("  help      - show this help")
    print("  quit      - exit the program")


def main():
    nr_1 = input_number('nr_1: ')
    nr_2 = input_number('nr_2: ')

    commands = {
        'multiply': lambda: multiply(nr_1, nr_2),
        'add': lambda: add(nr_1, nr_2),
        'difference': lambda: subtract(nr_1, nr_2),
        'division': lambda: divide(nr_1, nr_2),
        'all': lambda: all_ops(nr_1, nr_2),
    }

    print("Type 'help' to see available commands.")
    while True:
        cmd = input('cmd: ').strip().lower()
        if not cmd:
            continue
        if cmd in commands:
            result = commands[cmd]()
            print(result)
        elif cmd == 'change':
            nr_1 = input_number('nr_1: ')
            nr_2 = input_number('nr_2: ')
            # update the lambdas to capture new values
            commands['multiply'] = lambda: multiply(nr_1, nr_2)
            commands['add'] = lambda: add(nr_1, nr_2)
            commands['difference'] = lambda: subtract(nr_1, nr_2)
            commands['division'] = lambda: divide(nr_1, nr_2)
            commands['all'] = lambda: all_ops(nr_1, nr_2)
            print('The numbers have been changed.')
        elif cmd in ('quit', 'exit'):
            print('Thank you for using this program!')
            break
        elif cmd == 'help':
            print_help()
        else:
            print('Command unknown. Type "help" to see available commands.')


if __name__ == '__main__':
    main()
