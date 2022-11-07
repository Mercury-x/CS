def test_generator(x):
    while x < 100:
        yield x
        x += 10
    yield x


def cut_down(x):
    while x >= 1:
        yield x
        x -= 1


def cut_down2(x):
    if x > 0:
        yield x
        yield from yield_2()


def yield_2():
    yield 'first'
    yield 'second'


# t = test_generator(3)
#
# print(list(cut_down(9)))
# print(list(cut_down2(7)))
# print(yield_2())


class LettersIter:
    def __init__(self, start='a', end='e'):
        self.next_letter = start
        self.end = end

    def __next__(self):
        if self.next_letter == self.end:
            raise StopIteration
        letter = self.next_letter
        self.next_letter = chr(ord(letter) + 1)
        return letter

    def __iter__(self):
        start = self.next_letter
        while start < self.end:
            yield start
            start = chr(ord(start) + 1)


class Letters:
    def __init__(self, start='a', end='b'):
        self.start = start
        self.end = end

    def __iter__(self):
        return LettersIter(self.start, self.end)


letter_iter = Letters('d', 'r')
first_iterator = iter(letter_iter)
t1 = iter(first_iterator)
t2 = iter(first_iterator)
print(iter(first_iterator) == iter(first_iterator))  # False
print(t1)  # <generator object LettersIter.__iter__ at 0x00000238211D9938>
print(t2)  # <generator object LettersIter.__iter__ at 0x00000238211D9938>
print(next(first_iterator))  # d
print(next(iter(first_iterator)))  # e


# y2 = yield_2()
# y2_it = iter(y2)
# print(y2 == y2_it)
# print(next(first_iterator))
# print(iter(first_iterator))
# print([k for k in first_iterator])

def add_this_many(x, el, s):
    """ Adds el to the end of s the number of times x occurs in s.
    >>> s = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5]
    >>> add_this_many(2, 2, s)
    >>> s
    [1, 2, 4, 2, 1, 5, 5, 2, 2]
    """
    "*** YOUR CODE HERE ***"
    s_len = len(s)
    cnt = 0
    for i in range(s_len):
        if s[i] == x:
            cnt += 1
    s.extend([el for i in range(cnt)])
