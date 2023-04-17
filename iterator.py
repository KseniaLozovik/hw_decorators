import types
from logger import logger2
class FlatIterator:

    def __init__(self, list_of_list):
        self.n = -1
        self.list_of_list = list_of_list

    def __iter__(self):
        self.flat_list = []
        self.flat_iter = iter(self.flat_list)
        for group in self.list_of_list:
            self.flat_list.extend(group)
        return self

    def __next__(self):
        self.n += 1
        if self.n == len(self.flat_list):
            raise StopIteration

        return next(self.flat_iter)


@logger2('iter_log.log')
def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
        # print('ok4')

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    # print('ok5')


def flat_generator(list_of_lists):
    flat_list = []
    for item in list_of_lists:
        flat_list.extend(item)
    for i in flat_list:
        yield i


@logger2('iter_log.log')
def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item
        # print('ok')
    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    # print('ok2')
    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    # print('ok3')

if __name__ == '__main__':
    test_2(), test_1()