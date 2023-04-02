import pytest

# Create and reverse dictionary


dict_numbers = {'one': 1, 'two': 2, 'three': 3}
reversed_dict = {value: key for key, value in dict_numbers.items()}


# Convert dictionary to answer.txt
def convert_to_txt(dic):
    with open('answer.txt', 'w') as f:
        for key, value in dic.items():
            f.write(f'{key}: {value}\n')


# Rename file based on OS
import os


def rename_file():
    system = os.name
    new_filenames = {
        'nt': 'windows.txt',
        'posix': {
            'Linux': 'linux.txt',
            'Darwin': 'mac.txt',
        },
    }
    if system in new_filenames:
        if isinstance(new_filenames[system], str):
            os.rename('test.txt', new_filenames[system])
        elif os.uname().sysname in new_filenames[system]:
            os.rename('test.txt', new_filenames[system][os.uname().sysname])
    else:
        print('Unknown operating system')


# Increment generator
def increment_generator(start, stop):
    step = 1 if stop > start else -1
    while start != stop:
        yield start
        start += step
    yield stop


class A:
    name = 'A'

    @classmethod
    def print_name(cls):
        print(cls.name)


class B(A):
    name = 'B'


class C(B):
    name = 'C'

    def __init__(self):
        super().__init__()
        print(super().name)


def example_args_func(*args):
    for arg in args:
        print(arg)


def example_kwargs_func(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}={value}")


import json


def update_json_file(file_name, key, new_value):
    with open(file_name, 'r') as f:
        data = json.load(f)
    data[key] = new_value
    with open(file_name, 'w') as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    # convert_to_txt(reversed_dict)
    # rename_file()
    # for i in increment_generator(10, -5):
    #     print(i)
    # example_args_func(1, 2, 3, 4, 5, 6)
    # example_kwargs_func(name='Andriy', surname='Kozachok', age='21', city='Kyiv')
    update_json_file('person_info.json', 'age', 22)
