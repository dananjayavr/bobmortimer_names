import random

def get_names_from_file(file):
    """
    Get names from file
    """
    names = []
    with open(file, 'r') as f:
        for line in f:
            names.append(line.strip())
    return names


def choose_random_name(names):
    """
    Choose random name from list
    """
    return random.choice(names)


if __name__ == '__main__':
    names = get_names_from_file('names.txt')
    for i in range(1):
        print(choose_random_name(names))